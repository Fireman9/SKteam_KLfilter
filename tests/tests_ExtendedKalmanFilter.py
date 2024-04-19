import unittest
import numpy as np
from ExtendedKalmanFilter import ExtendedKalmanFilter


class TestExtendedKalmanFilter(unittest.TestCase):
    """
    A test case class for testing the ExtendedKalmanFilter class.

    This class contains test methods to verify the functionalities of the ExtendedKalmanFilter class.

    Methods:
        setUp(): Initializes an ExtendedKalmanFilter object before each test method is executed.
        test_init(): Tests the initialization of the ExtendedKalmanFilter object.
        test_update(): Tests the update method of the ExtendedKalmanFilter class.
        test_predict(): Tests the predict method of the ExtendedKalmanFilter class.
        test_x(): Tests the x property of the ExtendedKalmanFilter class.
    """

    def setUp(self):
        """
        Initializes an ExtendedKalmanFilter object before each test method is executed.
        """
        x = np.matrix([[0.5], [0.0]])
        F = np.matrix([[1, 0], [0, 0.9]])
        B = np.matrix([[-1], [0.1]])
        P = np.matrix([[0.1, 0], [0, 0.1]])
        Q = np.matrix([[0.01, 0], [0, 0.01]])
        R = 0.01
        def Hx(x): return x[0, 0]
        def HJacobian(x): return np.matrix([[1, 0]])
        self.ekf = ExtendedKalmanFilter(x, F, B, P, Q, R, Hx, HJacobian)

    def test_init(self):
        """
        Tests the initialization of the ExtendedKalmanFilter object.
        """
        self.assertTrue(np.array_equal(self.ekf._x, np.matrix([[0.5], [0.0]])))
        self.assertTrue(np.array_equal(
            self.ekf._F, np.matrix([[1, 0], [0, 0.9]])))
        self.assertTrue(np.array_equal(self.ekf._B, np.matrix([[-1], [0.1]])))
        self.assertTrue(np.array_equal(
            self.ekf._P, np.matrix([[0.1, 0], [0, 0.1]])))
        self.assertTrue(np.array_equal(
            self.ekf._Q, np.matrix([[0.01, 0], [0, 0.01]])))
        self.assertEqual(self.ekf._R, 0.01)

    def test_update(self):
        """
        Tests the update method of the ExtendedKalmanFilter class.
        """
        self.ekf.update(0.6)
        self.assertAlmostEqual(self.ekf._x[0, 0], 0.6, delta=0.001)

    def test_predict(self):
        """
        Tests the predict method of the ExtendedKalmanFilter class.
        """
        self.ekf.predict(0.1)
        self.assertAlmostEqual(self.ekf._x[0, 0], 0.4, delta=0.001)

    def test_x(self):
        """
        Tests the x property of the ExtendedKalmanFilter class.
        """
        self.assertTrue(np.array_equal(self.ekf.x, np.matrix([[0.5], [0.0]])))


if __name__ == '__main__':
    unittest.main()
