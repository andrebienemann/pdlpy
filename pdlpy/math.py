from math import e, erf, factorial, pi, sqrt


def ncr(n: int, r: int) -> int:
    return factorial(n) // (factorial(r) * factorial(n - r))
