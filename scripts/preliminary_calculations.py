"""Ön tasarım hesap örnekleri. Motor simülasyonu veya parça uygunluk testi değildir.

Standart Python 3 ile çalışır. Varsayımlar aşağıda görünürdür; bilinmeyen gerçek
motor/batarya özelliklerini otomatik tamamlamaz. Rapor değerlerini tekrar üretir.
"""
import json
import math


def examples():
    assumptions = {
        "user_nominal_bus_V": 72.0,
        "illustrative_max_bus_V_not_actual_pack": 87.6,
        "user_nominal_battery_current_A_assumed": 50.0,
        "reported_speed_rpm": 528.597,
        "reported_torque_Nm": 54.203,
        "reported_input_W": 3317.8,
        "reported_output_W": 3000.4,
        "example_phase_current_A": 100.0,
        "example_shunt_ohm": 0.0005,
        "example_CSA_gain": 20.0,
        "example_reference_V": 1.65,
        "example_Cbus_F": 0.001,
        "example_Rpre_ohm": 100.0,
        "example_Rdis_ohm": 10000.0,
        "example_discharge_target_V": 60.0,
        "example_MOSFET_R25_ohm": 0.0057,
        "example_hot_R_multiplier": 2.0,
        "example_parallel_count": 2,
    }
    a = assumptions
    v = a["illustrative_max_bus_V_not_actual_pack"]
    c = a["example_Cbus_F"]
    i = a["example_phase_current_A"]
    rs = a["example_shunt_ohm"]
    gain = a["example_CSA_gain"]
    ref = a["example_reference_V"]
    results = {
        "shaft_power_from_torque_speed_W": a["reported_torque_Nm"] * 2 * math.pi * a["reported_speed_rpm"] / 60,
        "reported_efficiency_fraction": a["reported_output_W"] / a["reported_input_W"],
        "conditional_DC_current_from_input_A": a["reported_input_W"] / a["user_nominal_bus_V"],
        "nominal_DC_power_72V_50A_W": 72 * 50,
        "shunt_power_if_100A_continuous_W": i * i * rs,
        "CSA_low_high_V_at_plus_minus_100A": [ref - i * rs * gain, ref + i * rs * gain],
        "CSA_gain50_invalid_range_V": [ref - i * rs * 50, ref + i * rs * 50],
        "two_active_switch_groups_conduction_W_100A": 2 * i * i * a["example_MOSFET_R25_ohm"] * a["example_hot_R_multiplier"] / a["example_parallel_count"],
        "cap_energy_J": 0.5 * c * v * v,
        "precharge_initial_A": v / a["example_Rpre_ohm"],
        "precharge_initial_W": v * v / a["example_Rpre_ohm"],
        "precharge_95pct_time_s": -a["example_Rpre_ohm"] * c * math.log(0.05),
        "discharge_time_to_60V_s": a["example_Rdis_ohm"] * c * math.log(v / a["example_discharge_target_V"]),
        "discharge_initial_W": v * v / a["example_Rdis_ohm"],
        "illustrative_C_for_100A_100us_10V_F": 100 * 100e-6 / 10,
        "illustrative_overshoot_50nH_500A_per_us_V": 50e-9 * 500e6,
        "bootstrap_HB_before_overshoot_V": v + 12,
    }
    return {"status": "ILLUSTRATIVE_ONLY_NOT_DESIGN_RELEASE", "assumptions": a, "results": results}


if __name__ == "__main__":
    print(json.dumps(examples(), ensure_ascii=False, indent=2))
