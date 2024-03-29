# Battery.py
# This file defines a Battery class for simulating a battery's behavior using a Thevenin model.

import math as m
from utils import Polynomial


class Battery:
    """
    Battery class for simulating battery behavior using a Thevenin model.

    Attributes:
        total_capacity (float): Total capacity of the battery in Ah.
        actual_capacity (float): Remaining capacity of the battery in As.
        R0 (float): Ohmic resistance in the Thevenin model.
        R1 (float): Resistance in the RC parallel branch of the Thevenin model.
        C1 (float): Capacitance in the RC parallel branch of the Thevenin model.
        _current (float): Current flowing through the battery (positive for discharge).
        _RC_voltage (float): Voltage across the RC parallel branch of the Thevenin model.
        _OCV_model (Polynomial): Polynomial representation of the Open Circuit Voltage (OCV) as a function of State of Charge (SoC).
    """

    def __init__(self, total_capacity, R0, R1, C1):
        """
        Initializes a Battery object.

        Args:
            total_capacity (float): Total capacity of the battery in Ah.
            R0 (float): Ohmic resistance in the Thevenin model.
            R1 (float): Resistance in the RC parallel branch of the Thevenin model.
            C1 (float): Capacitance in the RC parallel branch of the Thevenin model.
        """
        # Сapacity in As
        self.total_capacity = total_capacity * 3600
        self.actual_capacity = self.total_capacity

        # Thevenin model : OCV + R0 + R1//C1
        self.R0 = R0
        self.R1 = R1
        self.C1 = C1

        self._current = 0
        self._RC_voltage = 0

        # Polynomial representation of OCV vs SoC
        self._OCV_model = Polynomial(
            [3.1400, 3.9905, -14.2391, 24.4140, -13.5688, -4.0621, 4.5056])

    def update(self, time_delta):
        """
        Updates the battery's state after a given time step.

        Args:
            time_delta (float): Time step in seconds.
        """
        self.actual_capacity -= self._current * time_delta
        exp_coeff = m.exp(-time_delta / (self.R1 * self.C1))
        self._RC_voltage *= exp_coeff
        self._RC_voltage += self.R1 * (1 - exp_coeff) * self._current

    @property
    def current(self):
        """
        Returns the current flowing through the battery (positive for discharge).
        """
        return self._current

    @current.setter
    def current(self, current):
        """
        Sets the current flowing through the battery (positive for discharge).

        Args:
            current (float): Current value in Amps.
        """
        self._current = current

    @property
    def voltage(self):
        """
        Returns the terminal voltage of the battery.
        """
        return self.OCV - self.R0 * self.current - self._RC_voltage

    @property
    def state_of_charge(self):
        """
        Returns the State of Charge (SoC) of the battery as a fraction between 0 and 1.
        """
        return self.actual_capacity / self.total_capacity

    @property
    def OCV_model(self):
        """
        Returns the polynomial representation of the Open Circuit Voltage (OCV) as a function of State of Charge (SoC).
        """
        return self._OCV_model

    @property
    def OCV(self):
        """
        Returns the Open Circuit Voltage (OCV) of the battery at the current State of Charge (SoC).
        """
        return self.OCV_model(self.state_of_charge)


if __name__ == '__main__':
    # Battery parameters
    capacity = 3.2  # Ah
    discharge_rate = 1  # C
    time_step = 10  # s
    cut_off_voltage = 2.5

    # Calculate the discharge current
    current = capacity * discharge_rate

    # Create a Battery object
    my_battery = Battery(capacity, 0.062, 0.01, 3000)
    my_battery.current = current

    # Initialize lists to store simulation data
    time = [0]
    SoC = [my_battery.state_of_charge]
    OCV = [my_battery.OCV]
    RC_voltage = [my_battery._RC_voltage]
    voltage = [my_battery.voltage]  # Define the voltage list

    # Simulate the battery discharge
    while my_battery.voltage > cut_off_voltage:
        my_battery.update(time_step)
        time.append(time[-1]+time_step)
        SoC.append(my_battery.state_of_charge)
        OCV.append(my_battery.OCV)
        RC_voltage.append(my_battery._RC_voltage)
        voltage.append(my_battery.voltage)

    # Plot the simulation results
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    # Plot settings
    ax1.set_title('')
    ax1.set_xlabel('SoC')
    ax1.set_ylabel('Voltage')

    ax1.plot(SoC, OCV, label="OCV")
    ax1.plot(SoC, voltage, label="Total voltage")
    ax1.legend()

    plt.show()
