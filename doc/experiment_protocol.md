# experiment_protocol.py Documentation

This document provides documentation for the `experiment_protocol.py` file, which defines a function to launch an experiment protocol for a battery.

## `launch_experiment_protocol` Function

The `launch_experiment_protocol` function simulates a battery charge and discharge experiment by calling an external callback function with the desired current values at each time step.

### Parameters

- `Q_tot (float)`: Total capacity of the battery in Ah.
- `time_step (float)`: Time step for the experiment in seconds.
- `experiment_callback (callable)`: A function that takes the current value as input and performs the necessary simulation or experiment steps.

### Experiment Parameters

- `charge_current_rate (float)`: Charge current rate in C for constant current charging.
- `discharge_current_rate (float)`: Discharge current rate in C for constant current discharging.
- `discharge_constants_stages_time (float)`: Time duration for constant discharge stages in seconds.
- `pulse_time (float)`: Time duration for each pulse in seconds.
- `total_pulse_time (float)`: Total time duration for pulse discharge stages in seconds.
- `high_cut_off_voltage (float)`: High cut-off voltage for charging in volts.
- `low_cut_off_voltage (float)`: Low cut-off voltage for discharging in volts.

### Example Usage

```python
from experiment_protocol import launch_experiment_protocol

# Define experiment callback function
def experiment_callback(current):
    # Perform simulation or experiment steps here
    return simulated_voltage

# Launch experiment protocol
Q_tot = 3.2  # Total capacity of the battery in Ah
time_step = 10  # Time step for the experiment in seconds
launch_experiment_protocol(Q_tot, time_step, experiment_callback)
```
This code will simulate a battery charge and discharge experiment using the specified parameters and the provided callback function.
