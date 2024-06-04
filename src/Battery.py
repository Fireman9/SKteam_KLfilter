# Battery.py
# This file defines a Battery class for simulating a battery's behavior using a Thevenin model.
import math as m
from polynomial import Polynomial
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class Battery:
    """
    Battery class for simulating battery behavior using a Thevenin model.
    """
    total_capacity: float  # Total capacity of the battery in Ah
    R0: float  # Ohmic resistance
    R1: float  # Resistance in the RC parallel branch 
    C1: float  # Capacitance in the RC parallel branch 
    current: float = 0.0  # Current flowing through the battery (positive for discharge)
    _RC_voltage: float = 0.0  # Voltage across the RC parallel branch 
    _OCV_model: Polynomial = Polynomial([3.1400, 3.9905, -14.2391, 24.4140, -13.5688, -4.0621, 4.5056])  
    # Polynomial representation of the  (OCV) as a function of (SoC)

    def __post_init__(self):
        self.total_capacity *= 3600  # Convert Ah to As
        self.actual_capacity = self.total_capacity  # Remaining capacity of the battery in As

    def update(self, time_delta: float) -> None:
        """
        upd the battery's state after a given time step
        """
        self.actual_capacity -= self.current * time_delta
        exp_coeff = m.exp(-time_delta / (self.R1 * self.C1))
        self._RC_voltage *= exp_coeff
        self._RC_voltage += self.R1 * (1 - exp_coeff) * self.current

    @property
    def voltage(self) -> float:
        """
        returns the terminal voltage of the battery
        """
        return self.OCV - self.R0 * self.current - self._RC_voltage

    @property
    def state_of_charge(self) -> float:
        """
        returns SoC of the battery as a fraction between 0 and 1.
        """
        return self.actual_capacity / self.total_capacity

    @property
    def OCV_model(self) -> Polynomial:
        """
        returns the polynomial representation of the OCV as a function of SoC
        """
        return self._OCV_model

    @property
    def OCV(self) -> float:
        """
        return the OCV of the battery at the current SoC
        """
        return self.OCV_model(self.state_of_charge)

if __name__ == '__main__':
    capacity = 3.2  # Ah
    discharge_rate = 1  # C
    time_step = 10  # s
    cut_off_voltage = 2.5

    current = capacity * discharge_rate

    my_battery = Battery(capacity, 0.062, 0.01, 3000)
    my_battery.current = current

    time = [0]
    SoC = [my_battery.state_of_charge]
    OCV = [my_battery.OCV]
    RC_voltage = [my_battery._RC_voltage]
    voltage = [my_battery.voltage]  # voltage list

    # simulating the battery discharge
    while my_battery.voltage > cut_off_voltage:
        my_battery.update(time_step)
        time.append(time[-1]+time_step)
        SoC.append(my_battery.state_of_charge)
        OCV.append(my_battery.OCV)
        RC_voltage.append(my_battery._RC_voltage)
        voltage.append(my_battery.voltage)


    plt.xlim(0,1)
    plt.plot(SoC, OCV, label="OCV")
    plt.plot(SoC, voltage, label="Total voltage")
    plt.legend()

    plt.show()
