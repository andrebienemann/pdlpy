import math

from pdlpy.distribution import Distribution


class Normal(Distribution):
    """
    Continuous probability distribution of the random variable X that is assumed to be additively produced by many small effects
    """

    def __init__(self, mean, var):
        """
        Paramters
        mean: the expectation of the distribution
        var: the variance of the distribution
        """
        self._mean = mean
        self._var = var

    def __str__(self):
        mean = round(self._mean, 2)
        var = round(self._var, 2)
        return f"Normal(mean={mean}, var={var})"

    def pdf(self, x):
        """
        Probability Density Function

        Paramters
        x: a value of random variable X

        Returns
        the relative likelihood that a value of X would lie in sample space
        """
        return (1 / math.sqrt(2 * math.pi * self._var)) * math.e ** (
            -((x - self._mean) ** 2 / 2 * self._var)
        )

    def cdf(self, x):
        """
        Cumulative Distribution Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value less than or equal to x
        """
        return (1 + math.erf((x - self._mean) / (math.sqrt(self._var * 2)))) / 2
