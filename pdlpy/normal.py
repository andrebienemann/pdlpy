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
        self.__mean = mean
        self.__var = var

    @property
    def mean(self):
        return self.__mean

    @property
    def var(self):
        return self.__var

    def pdf(self, x):
        """
        Probability Density Function

        Paramters
        x: a value of random variable X

        Returns
        the relative likelihood that a value of X would lie in sample space
        """
        return (1 / math.sqrt(2 * math.pi * self.__var)) * math.e ** (
            -((x - self.__mean) ** 2 / 2 * self.__var)
        )

    def cdf(self, x):
        """
        Cumulative Distribution Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value less than or equal to x
        """
        return (1 + math.erf((x - self.__mean) / (math.sqrt(self.__var * 2)))) / 2
