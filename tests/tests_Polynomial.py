import unittest
from Polynomial import Polynomial


class TestPolynomial(unittest.TestCase):
    """
    A test case class for testing the Polynomial class.

    This class contains test methods to verify the functionalities of the Polynomial class.

    Methods:
        setUp(): Initializes a Polynomial object before each test method is executed.
        test_init(): Tests the initialization of the Polynomial object.
        test_call(): Tests the __call__ method of the Polynomial class.
        test_deriv(): Tests the deriv property of the Polynomial class.
    """

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
