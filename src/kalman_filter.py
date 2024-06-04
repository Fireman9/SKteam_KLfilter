# ExtendedKalmanFilter.py
# This file defines an ExtendedKalmanFilter dataclass for implementing the Extended Kalman Filter algorithm.

from dataclasses import dataclass
from typing import Callable
import numpy as np
from numpy import ndarray


@dataclass
class ExtendedKalmanFilter:
    """
        x: init state estimate
        F: state transition matrix
        B: input matrix
        P: initial state covariance matrix
        Q: process noise covariance matrix
        R: measurement noise covariance
        Hx: measurement function
        HJacobian: Jacobian of the measurement function
    """
    _x: ndarray
    _F: ndarray
    _B: ndarray
    _P: ndarray
    _Q: ndarray
    _R: float
    _Hx: Callable[[ndarray], float]
    _HJacobian: Callable[[ndarray], ndarray]

    def update(self, z: float) -> None:
        """
        Update the state estimate based on the measurement (z)
        """
        P = self._P
        R = self._R
        x = self._x
        H = self._HJacobian(x)
        S = H @ P @ H.T + R
        K = P @ H.T @ np.linalg.inv(S)  
        self._K = K  # storing the Kalman gain for debugging

        hx = self._Hx(x)
        y = float(z) - hx

        self._x = x + K * y
        KH = K @ H
        I_KH = np.eye(KH.shape[1]) - KH
        self._P = I_KH @ P @ I_KH.T + K * R * K.T

    def predict(self, u: float = 0) -> None:
        """
        Predict the next state estimate (where u is control input)
        """
        self._x = self._F @ self._x + self._B * float(u)
        self._P = self._F @ self._P @ self._F.T + self._Q

    @property
    def x(self) -> ndarray:
        return self._x