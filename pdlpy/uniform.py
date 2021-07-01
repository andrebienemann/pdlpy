from pdlpy.distribution import Distribution


class Uniform(Distribution):
    """
    Continuous distribution of a random variable X in interval [a; b] where any value of X has an equal probability
    """

    def __init__(self, a, b):
        """
        Paramters
        a: the minimum value of X
        b: the maximum value of X
        """
        self._a = a
        self._b = b
        self._mean = (a + b) / 2
        self._var = (b - a) ** 2 / 12

    def __str__(self):
        a = round(self._a, 2)
        b = round(self._b, 2)
        mean = round(self._mean, 2)
        var = round(self._var, 2)
        return f"Uniform(a={a}, b={b}, mean={mean}, var={var})"

    def pdf(self, x=None):
        """
        Probability Density Function

        Paramters
        x: a value of random variable X

        Returns
        the relative likelihood that a value of X would lie in sample space
        """
        return 1 / (self._b - self._a)

    def cdf(self, x):
        """
        Cumulative Distribution Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value less than or equal to x
        """
        if x <= self._a:
            return 0.0
        elif x >= self._b:
            return 1.0
        else:
            return (x - self._a) / (self._b - self._a)
