from math import ceil, e, erf, factorial, floor, log, log2, pi, sqrt


def ncr(n: int, r: int) -> int:
    return factorial(n) // (factorial(r) * factorial(n - r))
