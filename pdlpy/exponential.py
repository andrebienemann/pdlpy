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
        self.rate = rate
        self.mean = rate ** -1
        self.var = rate ** -2

    def pdf(self, x):
        """
        Probability Density Function

        Paramters
        x: a value of random variable X

        Returns
        the relative likelihood that a value of X would lie in sample space
        """
        return self.rate * math.e ** (-self.rate * x)

    def cdf(self, x):
        """
        Cumulative Distribution Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value less than or equal to x
        """
        return 1 - math.e ** (-self.rate * x)
