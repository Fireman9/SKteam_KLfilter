import unittest
from Battery import Battery
from Polynomial import Polynomial


class TestBattery(unittest.TestCase):
    """
    A test case class for testing the Battery class.

    This class contains test methods to verify the functionalities of the Battery class.

    Methods:
        setUp(): Initializes a Battery object before each test method is executed.
        test_init(): Tests the initialization of the Battery object.
        test_update(): Tests the update method of the Battery class.
        test_current_getter_setter(): Tests the getter and setter methods for the current property of the Battery class.
        test_voltage(): Tests the voltage property of the Battery class.
        test_state_of_charge(): Tests the state_of_charge property of the Battery class.
        test_OCV_model(): Tests the OCV_model property of the Battery class.
        test_OCV(): Tests the OCV property of the Battery class.
    """

    def setUp(self):
        """
        Initializes a Battery object before each test method is executed.
        """
        self.battery = Battery(3.2, 0.062, 0.01, 3000)

    def test_init(self):
        """
        Tests the initialization of the Battery object.
        """
        self.assertEqual(self.battery.total_capacity, 3.2 * 3600)
        self.assertEqual(self.battery.actual_capacity,
                         self.battery.total_capacity)
        self.assertEqual(self.battery.R0, 0.062)
        self.assertEqual(self.battery.R1, 0.01)
        self.assertEqual(self.battery.C1, 3000)
        self.assertEqual(self.battery.current, 0)
        self.assertEqual(self.battery._RC_voltage, 0)

    def test_update(self):
        """
        Tests the update method of the Battery class.
        """
        self.battery.current = 1.0
        self.battery.update(10)
        self.assertAlmostEqual(self.battery.actual_capacity,
                               self.battery.total_capacity - 10.0, delta=0.001)

    def test_current_getter_setter(self):
        """
        Tests the getter and setter methods for the current property of the Battery class.
        """
        self.battery.current = 2.0
        self.assertEqual(self.battery.current, 2.0)

    def test_voltage(self):
        """
        Tests the voltage property of the Battery class.
        """
        self.battery.current = 1.0
        self.battery._RC_voltage = 0.1
        self.assertAlmostEqual(self.battery.voltage, self.battery.OCV - self.battery.R0 *
                               self.battery.current - self.battery._RC_voltage, delta=0.001)

    def test_state_of_charge(self):
        """
        Tests the state_of_charge property of the Battery class.
        """
        self.battery.actual_capacity = self.battery.total_capacity / 2
        self.assertEqual(self.battery.state_of_charge, 0.5)

    def test_OCV_model(self):
        """
        Tests the OCV_model property of the Battery class.
        """
        self.assertIsInstance(self.battery.OCV_model, Polynomial)

    def test_OCV(self):
        """
        Tests the OCV property of the Battery class.
        """
        self.assertAlmostEqual(
            self.battery.OCV, self.battery.OCV_model(1.0), delta=0.001)


if __name__ == '__main__':
    unittest.main()
