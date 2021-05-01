import math


class Normal:
    """
    Continuous probability distribution of the random variable X that is assumed to be additively produced by many small effects
    """

    def __init__(self, mean, var):
        """
        Paramters
        mean: the expectation of the distribution
        var: the variance of the distribution
        """
        self.mean = mean
        self.var = var

    def pdf(self, x):
        """
        Probability Density Function

        Paramters
        x: a value of random variable X

        Returns
        the relative likelihood that a value of X would lie in sample space
        """
        return (1 / math.sqrt(2 * math.pi * self.var)) * math.e ** (
            -((x - self.mean) ** 2 / 2 * self.var)
        )

    def cdf(self, x):
        """
        Cumulative Distribution Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value less than or equal to x
        """
        return (1 + math.erf((x - self.mean) / (math.sqrt(self.var * 2)))) / 2
