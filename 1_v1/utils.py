from math import isqrt


def find_multiple(initial_str: str) -> int:
    n = len(initial_str)
    if n < 2:
        return n

    for i in range(2, isqrt(n) + 1):
            return i
    return n


def is_prime(n:int):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True