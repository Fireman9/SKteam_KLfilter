# main.py
# This file defines the main function to simulate a battery and estimate its state using an Extended Kalman Filter.

import numpy as np
import math as m
from battery import Battery
from kalman_filter import ExtendedKalmanFilter as EKF
from experiment_protocol import launch_experiment_protocol


def init_EKF(R0, R1, C1, std_dev, time_step, Q_tot):
    """
    Configures and returns an instance of the Extended Kalman Filter (EKF) for battery state estimation.

    Args:
        R0 (float): Ohmic resistance in the Thevenin model.
        R1 (float): Resistance in the RC parallel branch of the Thevenin model.
        C1 (float): Capacitance in the RC parallel branch of the Thevenin model.
        std_dev (float): Standard deviation of the measurement noise.
        time_step (float): Time step for the experiment in seconds.
        Q_tot (float): Total capacity of the battery in Ah.

    Returns:
        EKF: An instance of the Extended Kalman Filter.
    """
    # Initial state (SoC is intentionally set to a wrong value)
    # x = [[SoC], [RC voltage]]
    x = np.matrix([[0.5],
                   [0.0]])

    exp_coeff = m.exp(-time_step / (C1 * R1))

    # State transition model
    F = np.matrix([[1, 0],
                  [0, exp_coeff]])

    # Control-input model
    B = np.matrix([[-time_step / (Q_tot * 3600)],
                   [R1 * (1 - exp_coeff)]])

    # Variance from std_dev
    var = std_dev ** 2

    # Measurement noise
    R = var

    # State covariance
    P = np.matrix([[var, 0],
                   [0, var]])

    # Process noise covariance matrix
    Q = np.matrix([[var / 50, 0],
                   [0, var / 50]])

    def HJacobian(x):
        return np.matrix([[battery_simulation.OCV_model.deriv(x[0, 0]), -1]])

    def Hx(x):
        return battery_simulation.OCV_model(x[0, 0]) - x[1, 0]

    return EKF(x, F, B, P, Q, R, Hx, HJacobian)


def plot_simulation_results(time, true_voltage, mes_voltage, true_SoC, estim_SoC, current):
    """
    Plots the results of the battery simulation.

    Args:
        time (list): List of time values.
        true_voltage (list): List of true battery voltages.
        mes_voltage (list): List of measured battery voltages.
        true_SoC (list): List of true battery state-of-charge values.
        estim_SoC (list): List of estimated battery state-of-charge values.
        current (list): List of current values.
    """
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)

    # Plot settings
    ax1.set_title('')
    ax1.set_xlabel('Time / s')
    ax1.set_ylabel('voltage / V')

    ax2.set_xlabel('Time / s')
    ax2.set_ylabel('Soc')

    ax3.set_xlabel('Time / s')
    ax3.set_ylabel('Current / A')

    ax1.plot(time, true_voltage, label="True voltage")
    ax1.plot(time, mes_voltage, label="Mesured voltage")
    ax2.plot(time, true_SoC, label="True SoC")
    ax2.plot(time, estim_SoC, label="Estimated SoC")
    ax3.plot(time, current, label="Current")

    ax1.legend()
    ax2.legend()
    ax3.legend()

    plt.show()


if __name__ == '__main__':
    # Total capacity
    Q_tot = 3.2

    # Thevenin model values
    R0 = 0.062
    R1 = 0.01
    C1 = 3000

    # Time period
    time_step = 10

    # Create a Battery object
    battery_simulation = Battery(Q_tot, R0, R1, C1)

    # Discharged battery
    battery_simulation.actual_capacity = 0

    # Measurement noise standard deviation
    std_dev = 0.015

    # Get configured EKF
    Kf = init_EKF(R0, R1, C1, std_dev, time_step, Q_tot)

    time = [0]
    true_SoC = [battery_simulation.state_of_charge]
    estim_SoC = [Kf.x[0, 0]]
    true_voltage = [battery_simulation.voltage]
    mes_voltage = [battery_simulation.voltage + np.random.normal(0, 0.1, 1)[0]]
    current = [battery_simulation.current]

    def update_simulation_step(actual_current):
        """
        Updates the battery simulation and the Extended Kalman Filter for the current time step.

        Args:
            actual_current (float): The current value for the current time step.

        Returns:
            float: The measured voltage for the current time step.
        """
        battery_simulation.current = actual_current
        battery_simulation.update(time_step)

        time.append(time[-1] + time_step)
        current.append(actual_current)
        true_voltage.append(battery_simulation.voltage)
        mes_voltage.append(battery_simulation.voltage +
                           np.random.normal(0, std_dev, 1)[0])

        Kf.predict(u=actual_current)
        Kf.update(mes_voltage[-1] + R0 * actual_current)

        true_SoC.append(battery_simulation.state_of_charge)
        estim_SoC.append(Kf.x[0, 0])

        return battery_simulation.voltage

    # Launch experiment
    launch_experiment_protocol(Q_tot, time_step, update_simulation_step)

    # Plot results
    plot_simulation_results(time, true_voltage, mes_voltage,
                            true_SoC, estim_SoC, current)
