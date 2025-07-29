import math

operation_cache = {}

def power(base, exp):
    """Calculates the power of a base raised to an exponent."""
    MAX_INPUT = 10**6
    MAX_RESULT = 1e100

    if base > MAX_INPUT or exp > MAX_INPUT:
        raise ValueError(f"Input values must be less than or equal to {MAX_INPUT} - Overflow risk")

    if base == 0 and exp == 0:
        raise ValueError("0 raised to the power of 0 is undefined")

    key = ('power', base, exp)
    
    if key in operation_cache:
        return operation_cache[key]
    
    try:
        result = base ** exp
    except OverflowError:
        raise ValueError("Result exceeds maximum limit - Overflow risk")

    operation_cache[key] = result
    
    return result

def fibonacci(n):
    """Calculates the nth Fibonacci number."""
    MAX_INPUT = 1476
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
    if n > MAX_INPUT:
        raise ValueError(f"n must be less than or equal to {MAX_INPUT} - Overflow risk")
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    result = b
    operation_cache[key] = result
    return result
    return b
    


def factorial(n :int) -> int:
    """Calculates the factorial of a number."""
    MAX_INPUT = 170
    key = ('factorial', n)

    if key in operation_cache:
        return operation_cache[key]
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    if n > MAX_INPUT: 
        raise ValueError(f"n must be less than or equal to {MAX_INPUT} - Overflow risk")
    else:
        result = math.factorial(n)

    operation_cache[key] = result
    return result
