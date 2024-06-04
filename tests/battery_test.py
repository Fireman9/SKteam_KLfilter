import unittest
from typing import Optional
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from battery import Battery
from polynomial import Polynomial


class TestBattery(unittest.TestCase):
    def setUp(self) -> None:
        self.battery = Battery(3.2, 0.062, 0.01, 3000) # some battery

    def test_init(self) -> None:
        """
        Verifies that the attributes are set correctly during object creation
        """
        self.assertEqual(self.battery.total_capacity, 3.2 * 3600)
        self.assertEqual(self.battery.actual_capacity, self.battery.total_capacity)
        self.assertEqual(self.battery.R0, 0.062)
        self.assertEqual(self.battery.R1, 0.01)
        self.assertEqual(self.battery.C1, 3000)
        self.assertEqual(self.battery.current, 0)
        self.assertEqual(self.battery._RC_voltage, 0)

    def test_update(self) -> None:
        """
        Sets the current and updates the battery state, then verifies the updated capacity
        """
        self.battery.current = 1.0
        self.battery.update(10)
        self.assertAlmostEqual(self.battery.actual_capacity, self.battery.total_capacity - 10.0, delta=0.001)

    def test_current_getter_setter(self) -> None:
        """
        Ensures that the current value can be set and retrieved correctly
        """
        self.battery.current = 2.0
        self.assertEqual(self.battery.current, 2.0)

    def test_OCV_model(self) -> None:
        """
        Verifies that the OCV_model is an instance of the Polynomial class
        """
        self.assertIsInstance(self.battery.OCV_model, Polynomial)

    def test_state_of_charge(self) -> None:
        """
        Calculates the expected state of charge and compares it with the actual value
        """
        self.battery.actual_capacity = self.battery.total_capacity / 2
        self.assertEqual(self.battery.state_of_charge, 0.5)

    def test_OCV(self) -> None:
        """
        Compares the OCV value with the expected value calculated using the OCV_model
        """
        self.assertAlmostEqual(self.battery.OCV, self.battery.OCV_model(1.0), delta=0.001)

    def test_voltage(self) -> None:
        """
        Sets the current and RC voltage, and compares the voltage with the expected value
        """
        self.battery.current = 1.0
        self.battery._RC_voltage = 0.1
        expected_voltage = self.battery.OCV - self.battery.R0 * self.battery.current - self.battery._RC_voltage
        self.assertAlmostEqual(self.battery.voltage, expected_voltage, delta=0.001)


if __name__ == '__main__':
    unittest.main()