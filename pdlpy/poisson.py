import math


class Poisson:
    """
    Discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space
    """

    def __init__(self, rate):
        """
        Parameters
        rate: the average number of events
        """
        self.__rate = rate
        self.__mean = rate
        self.__var = rate

    @property
    def mean(self):
        return self.__mean

    @property
    def var(self):
        return self.__var

    def pmf(self, x):
        """
        Probability Mass Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value exactly equal to x
        """
        return (self.__rate ** x) * (math.e ** (-self.__rate)) / math.factorial(x)

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
