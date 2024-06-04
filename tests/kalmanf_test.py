import unittest
import numpy as np
from typing import Callable
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from kalman_filter import ExtendedKalmanFilter

class TestExtendedKalmanFilter(unittest.TestCase):
    def setUp(self) -> None:
        # Initialize the ExtendedKalmanFilter with test data
        x: np.ndarray = np.array([[0.5], [0.0]])
        F: np.ndarray = np.array([[1, 0], [0, 0.9]])
        B: np.ndarray = np.array([[-1], [0.1]])
        P: np.ndarray = np.array([[0.1, 0], [0, 0.1]])
        Q: np.ndarray = np.array([[0.01, 0], [0, 0.01]])
        R: float = 0.01
        def Hx(x: np.ndarray) -> float: return x[0, 0]
        def HJacobian(x: np.ndarray) -> np.ndarray: return np.array([[1, 0]])
        self.ekf: ExtendedKalmanFilter = ExtendedKalmanFilter(x, F, B, P, Q, R, Hx, HJacobian)

    def test_init(self) -> None:
        # Test if the kalman filter is initialized correctly
        self.assertTrue(np.array_equal(self.ekf._x, np.array([[0.5], [0.0]])))
        self.assertTrue(np.array_equal(self.ekf._F, np.array([[1, 0], [0, 0.9]])))
        self.assertTrue(np.array_equal(self.ekf._B, np.array([[-1], [0.1]])))
        self.assertTrue(np.array_equal(self.ekf._P, np.array([[0.1, 0], [0, 0.1]])))
        self.assertTrue(np.array_equal(self.ekf._Q, np.array([[0.01, 0], [0, 0.01]])))
        self.assertEqual(self.ekf._R, 0.01)

    def test_update(self) -> None:
        self.ekf.update(0.6)
        self.assertAlmostEqual(self.ekf._x[0, 0], 0.59, delta=0.1)
        self.ekf.update(0.7)
        self.assertAlmostEqual(self.ekf._x[0, 0], 0.64, delta=0.1)

    def test_predict(self) -> None:
        self.ekf.predict(0.1)
        self.assertAlmostEqual(self.ekf._x[0, 0], 0.4, delta=0.001)
        self.ekf.predict(-0.2)
        self.assertAlmostEqual(self.ekf._x[0, 0], 0.6, delta=0.001)

    def test_x(self) -> None:
        # Test the x property to ensure it returns the correct state
        self.assertTrue(np.array_equal(self.ekf.x, np.array([[0.5], [0.0]])))
        self.ekf.update(0.8)
        print("self.ekf.x:", self.ekf.x)  
        self.assertTrue(np.array_equal(self.ekf.x, np.array([[0.77],[0.]])))

    def test_invalid_input(self) -> None:
        with self.assertRaises(ValueError):
            self.ekf.update('invalid')
        with self.assertRaises(ValueError):
            self.ekf.predict('invalid')

if __name__ == '__main__':
    unittest.main()