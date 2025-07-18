import math

operation_cache = {}

def power(base, exp):
    """Calculates the power of a base raised to an exponent."""
    key = ('power', base, exp)
    if key in operation_cache:
        return operation_cache[key]
    result = base ** exp
    operation_cache[key] = result
    return result

def fibonacci(n):
    """Calculates the nth Fibonacci number."""
    key = ('fibonacci', n)
    if key in operation_cache:
        return operation_cache[key]
    
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
    result = b
    operation_cache[key] = result
    return result
    return b
    


def factorial(n :int) -> int:
    """Calculates the factorial of a number."""
    key = ('factorial', n)
    if key in operation_cache:
        return operation_cache[key]
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    else:
        result = math.factorial(n)
    operation_cache[key] = result
    return result
