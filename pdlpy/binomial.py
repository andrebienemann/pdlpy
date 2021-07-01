from pdlpy.combinatorics import ncr


class Binomial:
    """
    Discrete probability distribution of a number of successes in a sequence of independent experiments
    """

    def __init__(self, n, p):
        """
        Parameters
        n: the size of the sequence
        p: the probability of success
        """
        self.__n = n
        self.__p = p
        self.__mean = n * p
        self.__var = n * p * (1 - p)

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
        return ncr(self.__n, x) * self.__p ** x * (1 - self.__p) ** (self.__n - x)

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
