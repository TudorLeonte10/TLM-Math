import math

def power(base, exp):
    """Calculates the power of a base raised to an exponent."""
    return base ** exp

def fibonacci(n):
    """Calculates the nth Fibonacci number."""
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b

def factorial(n :int) -> int:
    """Calculates the factorial of a number."""
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    return math.factorial(n)
