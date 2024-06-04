import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):
    def setUp(self):
        """
        Initializes a Polynomial object before each test method is executed.
        """
        self.poly = Polynomial([1, 2, 3, 4])

    def test_init(self):
        """
        Tests the initialization of the Polynomial object.
        """
        self.assertEqual(self.poly._coeffs, [1, 2, 3, 4])
        self.assertEqual(self.poly._deg, 3)

    def test_call(self):
        """
        Tests the __call__ method of the Polynomial class.
        """
        self.assertEqual(self.poly(0), 1)
        self.assertEqual(self.poly(1), 10)

    def test_deriv(self):
        """
        Tests the deriv property of the Polynomial class.
        """
        deriv_poly = self.poly.deriv
        self.assertEqual(deriv_poly._coeffs, [2, 6, 12])


if __name__ == '__main__':
    unittest.main()
