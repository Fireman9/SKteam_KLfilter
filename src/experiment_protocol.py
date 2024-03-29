# experiment_protocol.py
# This file defines a function to launch an experiment protocol for a battery.

def launch_experiment_protocol(Q_tot, time_step, experiment_callback):
    """
    Launches an experiment protocol for a battery.

    This function simulates a battery charge and discharge experiment by calling
    an external callback function (`experiment_callback`) with the desired current
    values at each time step.

    Args:
        Q_tot (float): Total capacity of the battery in Ah.
        time_step (float): Time step for the experiment in seconds.
        experiment_callback (callable): A function that takes the current value 
            as input and performs the necessary simulation or experiment steps.
    """
    # Define experiment parameters
    charge_current_rate = 0.5  # C
    discharge_current_rate = 1  # C
    discharge_constants_stages_time = 20 * 60  # s
    pulse_time = 60  # s
    total_pulse_time = 40 * 60  # s
    high_cut_off_voltage = 4.2
    low_cut_off_voltage = 2.5

    # Charge CC (Constant Current)
    current = -charge_current_rate * Q_tot
    voltage = 0
    while voltage < high_cut_off_voltage:
        voltage = experiment_callback(current)

    # Charge CV (Constant Voltage)
    while current < -0.1:
        # Pseudo current control to simulate CV charge
        if voltage > high_cut_off_voltage*1.001:
            current += 0.01 * Q_tot
        voltage = experiment_callback(current)

    # Discharge first stage
    time = 0
    current = discharge_current_rate * Q_tot
    while time < discharge_constants_stages_time:
        experiment_callback(current)
        time += time_step

    # Discharge pulses stage
    time = 0
    while time < total_pulse_time:
        time_low = 0
        current = 0
        while time_low < pulse_time:
            experiment_callback(current)
            time_low += time_step

        time_high = 0
        current = discharge_current_rate * Q_tot
        while time_high < pulse_time:
            experiment_callback(current)
            time_high += time_step

        time += time_low + time_high

    # Discharge last stage
    time = 0
    current = discharge_current_rate * Q_tot
    while time < discharge_constants_stages_time:
        experiment_callback(current)
        time += time_step
