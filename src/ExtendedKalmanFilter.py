# ExtendedKalmanFilter.py
# This file defines an ExtendedKalmanFilter class for implementing the Extended Kalman Filter algorithm.

import numpy as np
from numpy import zeros, eye


class ExtendedKalmanFilter(object):
    """
    Extended Kalman Filter class.

    This class implements the Extended Kalman Filter algorithm for state estimation of non-linear systems.

    Attributes:
        _x (numpy.ndarray): Current state estimate.
        _F (numpy.ndarray): State transition model.
        _B (numpy.ndarray): Control input model.
        _P (numpy.ndarray): Covariance matrix of the state estimate.
        _Q (numpy.ndarray): Process noise covariance matrix.
        _R (numpy.ndarray): Measurement noise covariance matrix.
        _Hx (callable): Function that maps the state to the measurement space.
        _HJacobian (callable): Function that computes the Jacobian of the measurement function.
    """

    def __init__(self, x, F, B, P, Q, R, Hx, HJacobian):
        """
        Initializes an ExtendedKalmanFilter object.

        Args:
            x (numpy.ndarray): Initial state estimate.
            F (numpy.ndarray): State transition model.
            B (numpy.ndarray): Control input model.
            P (numpy.ndarray): Initial covariance matrix of the state estimate.
            Q (numpy.ndarray): Process noise covariance matrix.
            R (numpy.ndarray): Measurement noise covariance matrix.
            Hx (callable): Function that maps the state to the measurement space.
            HJacobian (callable): Function that computes the Jacobian of the measurement function.
        """
        self._x = x
        self._F = F
        self._B = B
        self._P = P
        self._Q = Q
        self._R = R
        self._Hx = Hx
        self._HJacobian = HJacobian

    def update(self, z):
        """
        Updates the state estimate and covariance matrix using the measurement z.

        Args:
            z (numpy.ndarray): Measurement vector.
        """
        P = self._P
        R = self._R
        x = self._x
        H = self._HJacobian(x)
        S = H * P * H.T + R
        K = P * H.T * S.I
        self._K = K  # Store the Kalman gain for debugging

        hx = self._Hx(x)
        y = np.subtract(z, hx)

        self._x = x + K * y
        KH = K * H
        I_KH = np.identity((KH).shape[1]) - KH
        self._P = I_KH * P * I_KH.T + K * R * K.T

    def predict(self, u=0):
        """
        Predicts the next state estimate and covariance matrix using the control input u.

        Args:
            u (numpy.ndarray or scalar, optional): Control input vector. Default is 0.
        """
        self._x = self._F * self._x + self._B * u
        self._P = self._F * self._P * self._F.T + self._Q

    @property
    def x(self):
        """
        Returns the current state estimate.
        """
        return self._x
