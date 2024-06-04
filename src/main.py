# main.py
# This file defines the main function to simulate a battery and estimate its state using an Extended Kalman Filter.
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math as m


from battery import Battery
from kalman_filter import ExtendedKalmanFilter as EKF
from experiment_protocol import launch_experiment_protocol


def init_EKF(R0: float, R1: float, C1: float, 
             std_dev: float, time_step: float, Q_tot: float) -> 'EKF':
    """
    conf and returns an instance of the KF for battery state estimation
    """
    # init state (SoC is intentionally set to a wrong value)
    # x = [[SoC], [RC voltage]]
    x = np.matrix([[0.5],
                   [0.0]])

    exp_coeff = m.exp(-time_step / (C1 * R1))

    # state transition model
    F = np.matrix([[1, 0],
                  [0, exp_coeff]])

    # control-input model 
    B = np.matrix([[-time_step / (Q_tot * 3600)],
                   [R1 * (1 - exp_coeff)]])

    var = std_dev ** 2
    R = var

    # state covariance
    P = np.matrix([[var, 0],
                   [0, var]])

    # process noise covariance matrix
    Q = np.matrix([[var / 50, 0],
                   [0, var / 50]])

    def HJacobian(x):
        return np.matrix([[battery_simulation.OCV_model.deriv(x[0, 0]), -1]])

    def Hx(x):
        return battery_simulation.OCV_model(x[0, 0]) - x[1, 0]

    return EKF(x, F, B, P, Q, R, Hx, HJacobian)


def plot_simulation_results(time: np.ndarray, true_voltage: np.ndarray, mes_voltage: np.ndarray,
                            true_SoC: np.ndarray, estim_SoC: np.ndarray, current: np.ndarray) -> None:
    
    sns.set_style("whitegrid")
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    sns.lineplot(x=time, y=true_voltage, label="True Voltage", ax=ax1)
    sns.lineplot(x=time, y=mes_voltage, label="Measured Voltage", ax=ax1)
    ax1.set_ylabel('Voltage (V)')
    ax1.legend()

    sns.lineplot(x=time, y=true_SoC, label="True SoC", ax=ax2)
    sns.lineplot(x=time, y=estim_SoC, label="Estimated SoC", ax=ax2)
    ax2.set_ylabel('State of Charge')
    ax2.legend()

    sns.lineplot(x=time, y=current, label="Current", ax=ax3)
    ax3.set_xlabel('Time (s)')
    ax3.set_ylabel('Current (A)')
    ax3.legend()

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # total capacity
    Q_tot = 3.2

    # Thevenin model values
    R0 = 0.062
    R1 = 0.01
    C1 = 3000

    time_step = 10
    battery_simulation = Battery(Q_tot, R0, R1, C1)

    # Discharged battery
    battery_simulation.actual_capacity = 0
    std_dev = 0.015
    
    Kf = init_EKF(R0, R1, C1, std_dev, time_step, Q_tot)

    time = [0]
    true_SoC = [battery_simulation.state_of_charge]
    estim_SoC = [Kf.x[0, 0]]
    true_voltage = [battery_simulation.voltage]
    mes_voltage = [battery_simulation.voltage + np.random.normal(0, 0.1, 1)[0]]
    current = [battery_simulation.current]

    def update_simulation_step(actual_current: float) -> float:
        """
        Updates the battery simulation for the current time step
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

    launch_experiment_protocol(Q_tot, time_step, update_simulation_step)

    plot_simulation_results(time, true_voltage, mes_voltage,
                            true_SoC, estim_SoC, current)
