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
        self.n = n
        self.p = p
        self.mean = n * p
        self.var = n * p * (1 - p)

    def pmf(self, x):
        """
        Probability Mass Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value exactly equal to x
        """
        return ncr(self.n, x) * self.p ** x * (1 - self.p) ** (self.n - x)

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
