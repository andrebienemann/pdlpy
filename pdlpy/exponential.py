import math

from pdlpy.distribution import Distribution


class Exponential(Distribution):
    """
    Continuous probability distribution of time between events in a Poisson process
    """

    def __init__(self, rate):
        """
        Paramters
        rate: the average number of events
        """
        self._rate = rate
        self._mean = rate ** -1
        self._var = rate ** -2

    def __str__(self):
        rate = round(self._rate, 2)
        mean = round(self._mean, 2)
        var = round(self._var, 2)
        return f"Exponential(rate={rate}, mean={mean}, var={var})"

    def pdf(self, x):
        """
        Probability Density Function

        Paramters
        x: a value of random variable X

        Returns
        the relative likelihood that a value of X would lie in sample space
        """
        return self._rate * math.e ** (-self._rate * x)

    def cdf(self, x):
        """
        Cumulative Distribution Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value less than or equal to x
        """
        return 1 - math.e ** (-self._rate * x)
