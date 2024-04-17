import random

def construct_polynomial(s, k):
    """Construct a polynomial of degree k-1 with s as the constant term."""
    coefficients = [s] + [random.randint(0, 100) for _ in range(k-1)]
    return coefficients

def sum_polynomials(polynomials, k):
    """Sum up a list of polynomials."""
    summed_coefficients = [0] * k
    
    for poly in polynomials:
        for i, coeff in enumerate(poly):
            summed_coefficients[i] += coeff
            
    return summed_coefficients


def evaluate_polynomial(coefficients, x):
    """Evaluate the polynomial at a given point."""
    return sum([coeff * (x ** i) for i, coeff in enumerate(coefficients)])

def compute_l(i, k):
    """
    Compute the l(i).
    """
    product = 1
    for j in range(1, k+1):
        if j != i:
            product *= (- j) / (i - j)
    return product

def compute_average_with_shamir(data):
    """
    Reconstruct the sum of secrets.
    """
    n = len(data)
    k = n // 2
    polynomials = [construct_polynomial(s, k) for s in data]
    summed_coefficients = sum_polynomials(polynomials, k)
    secret_sum = 0
    for i in range(1, k+1):
        secret_sum += evaluate_polynomial(summed_coefficients, i) * compute_l(i, k)
    return secret_sum / n
