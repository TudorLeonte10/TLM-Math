import math
import time

operation_cache = {}

def power(base, exp):
    """Calculates the power of a base raised to an exponent."""
    start= time.perf_counter()
    key = ('power', base, exp)
    if key in operation_cache:
        end = time.perf_counter()
        print(f"Power Cached Execution Time: {(end-start)*1000:.9f} ms")
        return {
            "result": operation_cache[key],
            "execution_time_ms": (end - start) * 1000
        } 
    start = time.perf_counter()
    result = base ** exp
    operation_cache[key] = result
    end = time.perf_counter()
    print(f"Power Execution Time: {(end-start)*1000:.9f} ms")
    return {
        "result": result,
        "execution_time_ms": (end - start) * 1000
    }

def fibonacci(n):
    """Calculates the nth Fibonacci number."""
    start = time.perf_counter()
    key = ('fibonacci', n)
    if key in operation_cache:
        end = time.perf_counter()
        print(f"Fibonacci Cached Execution Time: {(end-start)*1000:.9f} ms")
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
    start = time.perf_counter()
    for _ in range(n-1):
        a, b = b, a + b
    result = b
    operation_cache[key] = result
    end = time.perf_counter()
    print(f"Fibonacci Execution Time: {(end-start)*1000:.9f} ms")
    return result
    


def factorial(n :int) -> int:
    """Calculates the factorial of a number."""
    start = time.perf_counter()
    key = ('factorial', n)
    if key in operation_cache:
        end = time.perf_counter()
        print(f"Factorial Cached Execution Time: {(end-start)*1000:.9f} ms")
        return operation_cache[key]
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    start = time.perf_counter()
    if n == 0 or n == 1:
        return 1
    else:
        result = math.factorial(n)
    end = time.perf_counter()
    print(f"Factorial Execution Time: {(end-start)*1000:.9f} ms")
    operation_cache[key] = result
    return result
