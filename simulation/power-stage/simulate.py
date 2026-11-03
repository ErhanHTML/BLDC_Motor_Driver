"""Simplified virtual three-phase inverter, not a device model or hardware validation.
Run offline: python simulate.py (requires numpy, matplotlib).
"""
from pathlib import Path
import csv, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
OUT=Path(__file__).resolve().parent
P={"v_source_V":72.0,"r_source_ohm":0.02,"c_bus_F":0.00136,
   "esr_bus_ohm":0.009,"f_pwm_Hz":15000.0,
   "f_electrical_Hz":60.0,"modulation_index":0.86,
   "deadtime_s":1.2e-6,"phase_L_H":450e-6,
   "phase_R_ohm":0.15,"back_emf_peak_V":22.0,
   "sim_length_s":0.06,"dt_s":1e-6}
dt=P["dt_s"]
times=np.arange(0,P["sim_length_s"],dt)
i=np.zeros(3); vcap=P["v_source_V"]
angles=np.arange(3)*(-2*np.pi/3)
T=[];V=[];IA=[];IB=[];IC=[];IBUS=[];ISRC=[]
for k,t in enumerate(times):
    tri=1-abs(2*((t*P["f_pwm_Hz"])%1)-1)
    d=0.5+P["modulation_index"]/2*np.sin(2*np.pi*P["f_electrical_Hz"]*t+angles)
    gap=P["deadtime_s"]*P["f_pwm_Hz"]
    hi=tri<(d-gap); lo=tri>(d+gap)
    # Simplified diode current paths when both devices are commanded OFF
    rail=np.where(hi,1.0,np.where(lo,0.0,(i<0).astype(float)))
    ibus=float(rail@i)
    isrc=(P["v_source_V"]-vcap+P["esr_bus_ohm"]*ibus)/(P["r_source_ohm"]+P["esr_bus_ohm"])
    icap=isrc-ibus
    vbus=vcap+P["esr_bus_ohm"]*icap
    nodes=rail*vbus
    neutral=np.mean(nodes)
    bemf=P["back_emf_peak_V"]*np.sin(2*np.pi*P["f_electrical_Hz"]*t+angles)
    di=(nodes-neutral-P["phase_R_ohm"]*i-bemf)/P["phase_L_H"]
    i+=dt*di
    i-=np.mean(i)
    vcap+=dt*icap/P["c_bus_F"]
    if k%10==0:
        T.append(t);V.append(vbus);IA.append(i[0]);IB.append(i[1]);IC.append(i[2])
        IBUS.append(ibus);ISRC.append(isrc)
T,V,IA,IB,IC,IBUS,ISRC=[np.array(z) for z in (T,V,IA,IB,IC,IBUS,ISRC)]
sel=T>=P["sim_length_s"]-1/P["f_electrical_Hz"]
metrics={"model":"idealized virtual time-step model, NOT device-level SPICE or hardware verification",
         "parameters":P,"Vbus_mean_V":round(float(np.mean(V[sel])),3),
         "Vbus_min_V":round(float(np.min(V[sel])),3),
         "Vbus_max_V":round(float(np.max(V[sel])),3),
         "Vbus_pp_V":round(float(np.ptp(V[sel])),3),
         "Iphase_A_rms_A":round(float(np.sqrt(np.mean(IA[sel]**2))),3),
         "Isource_avg_A":round(float(np.mean(ISRC[sel])),3),
         "Psource_avg_W":round(float(np.mean(ISRC[sel])*P["v_source_V"]),1)}
(OUT/"results.json").write_text(json.dumps(metrics,indent=2)+"\n")
with (OUT/"waveforms.csv").open("w",newline="") as f:
    w=csv.writer(f); w.writerow(["time_s","vbus_V","ia_A","ib_A","ic_A","ibus_A","isource_A"])
    w.writerows(zip(T,V,IA,IB,IC,IBUS,ISRC))
fig,axes=plt.subplots(3,1,figsize=(12,8),sharex=True)
axes[0].plot(1000*T,V); axes[0].set_ylabel("Vdc [V]")
for series,name in ((IA,"A"),(IB,"B"),(IC,"C")):
    axes[1].plot(1000*T,series,label=name)
axes[1].legend();axes[1].set_ylabel("Phase currents [A]")
axes[2].plot(1000*T,IBUS,label="DC link");axes[2].plot(1000*T,ISRC,label="Source")
axes[2].legend();axes[2].set_ylabel("DC current [A]")
axes[2].set_xlabel("Time [ms]")
for ax in axes: ax.grid(alpha=0.2)
fig.suptitle("Simplified virtual three-phase inverter (fictional motor plant)")
fig.tight_layout();fig.savefig(OUT/"waveforms.png",dpi=140)
print(json.dumps(metrics,indent=2))
