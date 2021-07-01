import math


class Exponential:
    """
    Continuous probability distribution of time between events in a Poisson process
    """

    def __init__(self, rate):
        """
        Paramters
        rate: the average number of events
        """
        self.__rate = rate
        self.__mean = rate ** -1
        self.__var = rate ** -2

    def __str__(self):
        rate = round(self.__rate, 2)
        mean = round(self.__mean, 2)
        var = round(self.__var, 2)
        return f"Exponential(rate={rate}, mean={mean}, var={var})"

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
        return self.__rate * math.e ** (-self.__rate * x)

    def cdf(self, x):
        """
        Cumulative Distribution Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value less than or equal to x
        """
        return 1 - math.e ** (-self.__rate * x)
