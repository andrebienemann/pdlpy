from math import ceil, e, erf, factorial, floor, log, pi, sqrt


def ncr(n: int, r: int) -> int:
    return factorial(n) // (factorial(r) * factorial(n - r))
