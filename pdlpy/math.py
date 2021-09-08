from math import e, erf, factorial, floor, pi, sqrt


def ncr(n: int, r: int) -> int:
    return factorial(n) // (factorial(r) * factorial(n - r))
