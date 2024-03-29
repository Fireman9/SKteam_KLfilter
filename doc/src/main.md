# main.py Documentation

This document provides documentation for the `main.py` file, which defines the main function to simulate a battery and estimate its state using an Extended Kalman Filter.

## Functions

### `init_EKF(R0, R1, C1, std_dev, time_step)`

Configures and returns an instance of the Extended Kalman Filter (EKF) for battery state estimation.

#### Parameters

- `R0 (float)`: Ohmic resistance in the Thevenin model.
- `R1 (float)`: Resistance in the RC parallel branch of the Thevenin model.
- `C1 (float)`: Capacitance in the RC parallel branch of the Thevenin model.
- `std_dev (float)`: Standard deviation of the measurement noise.
- `time_step (float)`: Time step for the experiment in seconds.
- `Q_tot (float)`: Total capacity of the battery in Ah.

#### Returns

- `EKF`: An instance of the Extended Kalman Filter.

### `plot_simulation_results(time, true_voltage, mes_voltage, true_SoC, estim_SoC, current)`

Plots the results of the battery simulation.

#### Parameters

- `time (list)`: List of time values.
- `true_voltage (list)`: List of true battery voltages.
- `mes_voltage (list)`: List of measured battery voltages.
- `true_SoC (list)`: List of true battery state-of-charge values.
- `estim_SoC (list)`: List of estimated battery state-of-charge values.
- `current (list)`: List of current values.

### Main Function

The main function simulates a battery and estimates its state using an Extended Kalman Filter.

#### Steps

1. Define battery parameters.
2. Initialize a Battery object.
3. Configure an Extended Kalman Filter (EKF).
4. Define lists to store simulation data.
5. Define a function to update the simulation step.
6. Launch the experiment protocol.
7. Plot the simulation results.

### Example Usage

```python
# Example usage of main.py
# Execute the main function to simulate battery behavior and estimate its state using an Extended Kalman Filter
python3 main.py
```

This code will simulate a battery and estimate its state, displaying the results in a plot.
