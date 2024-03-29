# Battery.py Documentation

This document provides documentation for the `Battery.py` file, which defines a Battery class for simulating battery behavior using a Thevenin model.

## Battery Class

The `Battery` class represents a battery and allows for simulation of its behavior using a Thevenin model.

### Attributes

- `total_capacity`: Total capacity of the battery in Ah.
- `actual_capacity`: Remaining capacity of the battery in As.
- `R0`: Ohmic resistance in the Thevenin model.
- `R1`: Resistance in the RC parallel branch of the Thevenin model.
- `C1`: Capacitance in the RC parallel branch of the Thevenin model.

### Methods

- `__init__(self, total_capacity, R0, R1, C1)`: Initializes a Battery object with the specified parameters.
- `update(self, time_delta)`: Updates the battery's state after a given time step.
- `current`: Property to get or set the current flowing through the battery.
- `voltage`: Property to get the terminal voltage of the battery.
- `state_of_charge`: Property to get the State of Charge (SoC) of the battery.
- `OCV_model`: Property to get the polynomial representation of the Open Circuit Voltage (OCV).
- `OCV`: Property to get the Open Circuit Voltage (OCV) of the battery.

### Example Usage

```python
from Battery import Battery

# Create a Battery object
my_battery = Battery(3.2, 0.062, 0.01, 3000)

# Set the current
my_battery.current = 1

# Update the battery's state
my_battery.update(10)

# Get battery information
print("State of Charge:", my_battery.state_of_charge)
print("Terminal Voltage:", my_battery.voltage)
```

This will output:
```
State of Charge: 1.0
Terminal Voltage: 3.14
```

