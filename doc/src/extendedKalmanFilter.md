# ExtendedKalmanFilter.py Documentation

This document provides documentation for the `ExtendedKalmanFilter.py` file, which defines an ExtendedKalmanFilter class for implementing the Extended Kalman Filter algorithm.

## ExtendedKalmanFilter Class

The `ExtendedKalmanFilter` class implements the Extended Kalman Filter algorithm for state estimation of non-linear systems.

### Attributes

- `_x (numpy.ndarray)`: Current state estimate.
- `_F (numpy.ndarray)`: State transition model.
- `_B (numpy.ndarray)`: Control input model.
- `_P (numpy.ndarray)`: Covariance matrix of the state estimate.
- `_Q (numpy.ndarray)`: Process noise covariance matrix.
- `_R (numpy.ndarray)`: Measurement noise covariance matrix.
- `_Hx (callable)`: Function that maps the state to the measurement space.
- `_HJacobian (callable)`: Function that computes the Jacobian of the measurement function.

### Methods

- `__init__(self, x, F, B, P, Q, R, Hx, HJacobian)`: Initializes an ExtendedKalmanFilter object with the specified parameters.
- `update(self, z)`: Updates the state estimate and covariance matrix using the measurement z.
- `predict(self, u=0)`: Predicts the next state estimate and covariance matrix using the control input u.

### Properties

- `x`: Returns the current state estimate.

### Example Usage

```python
import numpy as np

# Define functions for mapping state to measurement space and computing Jacobian
def Hx(x):
    return np.array([[x[0, 0]]])  # Example mapping function

def HJacobian(x):
    return np.array([[1]])  # Example Jacobian function

# Initialize ExtendedKalmanFilter object
x = np.array([[0]])  # Initial state estimate
F = np.array([[1]])  # State transition model
B = np.array([[0]])  # Control input model
P = np.array([[1]])  # Initial covariance matrix of the state estimate
Q = np.array([[0.01]])  # Process noise covariance matrix
R = np.array([[0.1]])  # Measurement noise covariance matrix
ekf = ExtendedKalmanFilter(x, F, B, P, Q, R, Hx, HJacobian)

# Update state estimate using measurement
z = np.array([[2]])  # Example measurement vector
ekf.update(z)

# Predict next state estimate using control input
u = 0  # Example control input
ekf.predict(u)

# Get current state estimate
current_state_estimate = ekf.x
print("Current State Estimate:", current_state_estimate)
```

This will output:

```
Current State Estimate: [[1.98]]
```
