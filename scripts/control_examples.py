#!/usr/bin/env python3
"""Educational amplitude-invariant FOC/SVPWM calculations; not motor firmware.

No measured motor parameters, dynamic plant, switching transients or Hall model.
Run: python3 scripts/control_examples.py
"""

from math import cos, sin, sqrt, pi, hypot, isclose, degrees


def abc_from_dq(id_a, iq_a, theta_rad):
    alpha = id_a * cos(theta_rad) - iq_a * sin(theta_rad)
    beta = id_a * sin(theta_rad) + iq_a * cos(theta_rad)
    return alpha, -alpha / 2 + sqrt(3) * beta / 2, -alpha / 2 - sqrt(3) * beta / 2


def dq_from_abc(ia, ib, ic, theta_rad):
    if not isclose(ia + ib + ic, 0, abs_tol=1e-9):
        raise ValueError("Three-wire current sum must be zero")
    alpha, beta = ia, (ia + 2 * ib) / sqrt(3)
    return alpha * cos(theta_rad) + beta * sin(theta_rad), -alpha * sin(theta_rad) + beta * cos(theta_rad)


def pi_sample(reference_a, measured_a, kp_v_per_a, ki_v_per_as, ts_s, integral_v):
    """One unsaturated sample with continuous-time Ki; no anti-windup here."""
    error = reference_a - measured_a
    next_integral = integral_v + ki_v_per_as * ts_s * error
    return kp_v_per_a * error + next_integral, next_integral


def svm_times(vref_v, angle_rad, vdc_v, ts_s):
    if vdc_v <= 0 or ts_s <= 0 or not 0 <= vref_v <= vdc_v / sqrt(3) + 1e-12:
        raise ValueError("Reference outside circular linear SVM region")
    angle_rad %= 2 * pi
    sector = min(5, int(angle_rad / (pi / 3)))
    local_angle = angle_rad - sector * pi / 3
    t1 = ts_s * sqrt(3) * vref_v / vdc_v * sin(pi / 3 - local_angle)
    t2 = ts_s * sqrt(3) * vref_v / vdc_v * sin(local_angle)
    return sector, t1, t2, ts_s - t1 - t2


def validate():
    # Compare physical phase invariants and forward/inverse transforms across a full turn.
    for id_a, iq_a in [(0, 10), (-5, 10), (2, 10), (0, -10)]:
        for n in range(360):
            theta = n * pi / 180
            abc = abc_from_dq(id_a, iq_a, theta)
            recovered = dq_from_abc(*abc, theta)
            assert isclose(sum(abc), 0, abs_tol=1e-10)
            assert isclose(sum(i * i for i in abc), 1.5 * (id_a * id_a + iq_a * iq_a), abs_tol=1e-9)
            assert all(isclose(a, b, abs_tol=1e-10) for a, b in zip(recovered, (id_a, iq_a)))

    # Independently reconstruct the reference from the two physical active vectors.
    for magnitude in [0, 20, 72 / sqrt(3)]:
        for n in range(360):
            theta = n * pi / 180
            sector, t1, t2, t0 = svm_times(magnitude, theta, 72, 50e-6)
            assert min(t1, t2, t0) >= -1e-15
            assert isclose(t1 + t2 + t0, 50e-6, abs_tol=1e-15)
            a1, a2 = sector * pi / 3, (sector + 1) * pi / 3
            alpha = (2 * 72 / 3) * (t1 * cos(a1) + t2 * cos(a2)) / 50e-6
            beta = (2 * 72 / 3) * (t1 * sin(a1) + t2 * sin(a2)) / 50e-6
            assert isclose(alpha, magnitude * cos(theta), abs_tol=1e-10)
            assert isclose(beta, magnitude * sin(theta), abs_tol=1e-10)

    volts, integral = pi_sample(10, 6, 0.8, 0.05, 50e-6, 2.5)
    assert isclose(volts, 5.70001, abs_tol=1e-12)
    assert isclose(integral, 2.50001, abs_tol=1e-12)
    # Explicit discrete Ki=0.05 V/A is equivalent to continuous Ki=1000 V/(A*s).
    assert isclose(pi_sample(10, 6, 0.8, 1000, 50e-6, 2.5)[0], 5.9)
    try:
        svm_times(50, 0, 72, 50e-6)
    except ValueError:
        pass
    else:
        raise AssertionError("Out-of-range reference was accepted")


def main():
    validate()
    print("PASS: dq/abc invariants (1440 points), SVM reconstruction (1080 points), PI units and voltage limit")
    print("All numbers below are educational examples, not measured motor results.")
    for theta_deg in [0, 90, 180, 270]:
        abc = abc_from_dq(0, 10, theta_deg * pi / 180)
        print(f"Id=0 Iq=10 theta={theta_deg:3d} deg -> abc=" + ", ".join(f"{i:+.6f} A" for i in abc))
    print("Id=2 Iq=10 theta=30 deg -> abc:", abc_from_dq(2, 10, pi / 6))
    print("Correct PI output / integral (V):", pi_sample(10, 6, 0.8, 0.05, 50e-6, 2.5))
    _, t1, t2, t0 = svm_times(20, pi / 6, 72, 50e-6)
    duty = ((t1 + t2 + t0 / 2) / 50e-6, (t2 + t0 / 2) / 50e-6, (t0 / 2) / 50e-6)
    print(f"SVM T1/T2/T0 (us): {t1*1e6:.6f} / {t2*1e6:.6f} / {t0*1e6:.6f}")
    print("SVM upper duty U/V/W:", duty)
    # Check the equivalent phase-neutral average independently of the dwell-time formula.
    common = sum(duty) / 3
    phases = tuple(72 * (d - common) for d in duty)
    alpha, beta = phases[0], (phases[0] + 2 * phases[1]) / sqrt(3)
    assert isclose(hypot(alpha, beta), 20, abs_tol=1e-10)
    print("SVM phase-neutral averages (V):", phases)
    print(f"SPWM max={72/2:.6f} V; SVM max={72/sqrt(3):.6f} V; 95% margin={.95*72/sqrt(3):.6f} V")
    print(f"Five 20 kHz periods={5*50:.0f} us; 14-bit count step={360/16384:.8f} mechanical deg")
    print(f"60 deg / 2 ms: omega_e={(pi/3)/.002:.6f} rad/s; p=4 -> rpm={((pi/3)/.002)/4*60/(2*pi):.3f}")
    print(f"10 us delay at 1 kHz electrical={degrees(2*pi*1000*10e-6):.3f} electrical deg")
    for delta in [2, 10, 30]:
        rad = delta * pi / 180
        print(f"Angle error {delta} deg: Id_true={-10*sin(rad):.6f} A Iq_true={10*cos(rad):.6f} A torque_ratio={cos(rad):.8f}")


if __name__ == "__main__":
    main()
