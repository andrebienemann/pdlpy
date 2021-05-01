from math import factorial


def ncr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))
