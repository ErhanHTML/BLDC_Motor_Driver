# Virtual power-stage simulation

Python/Numpy model only. Run with `python simulate.py` in a virtual software environment.

Model simplifications: ideal 3-phase switching and simplistic freewheel in dead time, fictional floating-star R/L/back EMF, lumped source resistance and link ESR/C. It **does not model actual MOSFET or driver**, thermal behavior, shoot-through, commutation overshoot, traction protection or EMI.

The source code produces a numerical trace, PNG and JSON. Checked reference output for the same assumptions: bus mean 71.692 V, peak-to-peak 0.366 V, phase A RMS 23.826 A, input approx. 1108 W. This is an intentionally **illustrative model**, NOT the target 3.5/5 kW operating point, and is not a qualifying hardware simulation.

The higher-power goals require a real motor plant and validated models; no live battery connection or device-level build instructions are part of this study.