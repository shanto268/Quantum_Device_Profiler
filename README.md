# Quantum Devices Profiler

# Setup:

## Configuration Files:

Configuration File Templates for all files

### Resonator Finder:

```json
{
  "expected_resonances":[floats], #GHz
  "res_type":[strings],
  "electrical_delay":float, #ns
  "IF_bandwidth":int, #KHz
  "averaging":int
}
```

for example


```json
{
  "expected_resonances":[5.456, 6.12],
  "res_type":["notch","reflection"],
  "electrical_delay":112,
  "IF_bandwidth":1,
  "averaging":10
}
```

### Instrument Server:


```json
{
  "instr_uid":"",
  "instr_name":"",
  "instr_config": {}
}
```

for example

```json
{
  "instr_uid": "RS_LO",
  "instr_name": "Rohde&Schwarz RF Source",
  "instr_config": {"interface":"TCPIP","address":"192.000.0.000","startup":"Get config")}
}
```


---

## Functionality Needed:

**At Zero Flux**

- [ ] Find Resonances through Interfacing with VNA
- [ ] Use `resonator_profiling.py` to fit the resonances and record the stats
- [ ] Take a Power Sweep with VNA and DA for each resonance and record the power at which the resonance goes non-linear and power required for 1 photon
- [ ] Check for flux tunability through VNA and SMU


- [ ] Take a flux sweep with VNA and SMU
- [ ] Fit the flux curve and extract parameters of interest

### Extra Functionality for NBR Devices:

- [ ] Check for QP trapping (i.e. Multiple Lorentzian peaks test)
- [ ] Power Sweep at finite flux
- [ ] Test for QP clearing using an LO, VNA and SMU (i.e. sharpening of resonance)

### Extra Functionality for Dissipator Devices:

### Extra Functionality for JPA:

### Extra Functionality for TWPA:

