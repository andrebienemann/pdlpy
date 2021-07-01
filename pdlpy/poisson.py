import math

from pdlpy.distribution import Distribution


class Poisson(Distribution):
    """
    Discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space
    """

    def __init__(self, rate):
        """
        Parameters
        rate: the average number of events
        """
        self._rate = rate
        self._mean = rate
        self._var = rate

    def __str__(self):
        rate = round(self._rate, 2)
        mean = round(self._mean, 2)
        var = round(self._var, 2)
        return f"Poisson(rate={rate}, mean={mean}, var={var})"

    def pmf(self, x):
        """
        Probability Mass Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value exactly equal to x
        """
        return (self._rate ** x) * (math.e ** (-self._rate)) / math.factorial(x)

    def cdf(self, x):
        """
        Cumulative Distribution Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value less than or equal to x
        """
        if x == 0:
            return self.pmf(0)
        else:
            return self.pmf(x) + self.cdf(x - 1)
