from pdlpy.distribution import Distribution
from pdlpy.math import e, erf, pi, sqrt


class Normal(Distribution):
    """
    Continuous probability distribution of the random variable X that is assumed to be additively produced by many small effects
    """

    def __init__(self, mean: float, var: float):
        """
        Paramters
        mean: the expectation of the distribution
        var: the variance of the distribution
        """
        self._mean = mean
        self._var = var

    def __str__(self):
        return (
            "Normal(" 
            f"mean={self._mean:.2f}, " 
            f"var={self._var:.2f}" 
            ")"
        )

    def pdf(self, x: float) -> float:
        """
        Probability Density Function

        Paramters
        x: a value of random variable X

        Returns
        the relative likelihood that a value of X would lie in sample space
        """
        return (1 / sqrt(2 * pi * self._var)) * e ** (
            -((x - self._mean) ** 2 / 2 * self._var)
        )

    def cdf(self, x: float) -> float:
        """
        Cumulative Distribution Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value less than or equal to x
        """
        return (1 + erf((x - self._mean) / (sqrt(self._var * 2)))) / 2
