# Polynomial.py
# This file defines a Polynomial class for representing and manipulating polynomials.

class Polynomial:
    """
    Polynomial class for representing and manipulating polynomials.

    Attributes:
        _coeffs (list): List of coefficients of the polynomial.
        _deg (int): Degree of the polynomial.

    Methods:
        __call__(x): Evaluates the polynomial at the given value of x.
        deriv: Returns the derivative of the polynomial as a new Polynomial object.
    """

    def __init__(self, coeffs):
        """
        Initializes a Polynomial object.

        Args:
            coeffs (list): List of coefficients of the polynomial.
        """
        self._coeffs = coeffs
        self._deg = len(coeffs) - 1

    def __call__(self, x):
        """
        Evaluates the polynomial at the given value of x.

        Args:
            x (float or int): Value at which to evaluate the polynomial.

        Returns:
            float: Value of the polynomial at x.
        """
        value = 0
        for i, coeff in enumerate(self._coeffs):
            value += coeff * x ** i
        return value

    @property
    def deriv(self):
        """
        Returns the derivative of the polynomial as a new Polynomial object.

        Returns:
            Polynomial: The derivative of the polynomial.
        """
        d_coeffs = [0] * self._deg
        for i in range(self._deg):
            d_coeffs[i] = (i + 1) * self._coeffs[i + 1]
        return Polynomial(d_coeffs)


if __name__ == '__main__':
    # Example 1: Polynomial with coefficient [0]
    my_poly = Polynomial([0])
    my_poly_deriv = my_poly.deriv
    print(my_poly._coeffs)
    print(my_poly_deriv._coeffs)
    print("Result:", my_poly(1))
    print("Result:", my_poly_deriv(1))

    # Example 2: Polynomial with coefficients [1, 2, 3, 4]
    my_poly = Polynomial([1, 2, 3, 4])
    my_poly_deriv = my_poly.deriv
    print(my_poly._coeffs)
    print(my_poly_deriv._coeffs)
    print("Result:", my_poly(1))
    print("Result:", my_poly_deriv(1))
