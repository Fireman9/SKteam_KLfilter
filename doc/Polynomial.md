# Polynomial.py Documentation

This document provides documentation for the `Polynomial.py` file, which defines a Polynomial class for representing and manipulating polynomials.

## Polynomial Class

The `Polynomial` class represents a polynomial and allows for evaluation and differentiation of polynomials.

### Attributes

- `_coeffs`: List of coefficients of the polynomial.
- `_deg`: Degree of the polynomial.

### Methods

- `__init__(self, coeffs)`: Initializes a Polynomial object with the specified coefficients.
- `__call__(self, x)`: Evaluates the polynomial at the given value of x.
- `deriv`: Returns the derivative of the polynomial as a new Polynomial object.

### Example Usage

```python
from Polynomial import Polynomial

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
```

This will output:

```
[0]
[]
Result: 0
Result: 0
[1, 2, 3, 4]
[2, 6, 12]
Result: 10
Result: 20
```

