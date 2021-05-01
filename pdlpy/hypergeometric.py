from pdlpy.combinatorics import ncr


class Hypergeometric:
    """
    Discrete probability distribution that describes the probability of successes in draws from a finite test set
    """

    def __init__(self, n, N, M):
        """
        Parameters
        n: the number of draws
        N: the size of the test set
        M: the number of successes
        """
        self.n = n
        self.N = N
        self.M = M
        self.mean = n * M / N
        self.var = n * M / N * (1 - M / N) * (N - n) / (N - 1)

    def pmf(self, x):
        """
        Probability Mass Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value exactly equal to x
        """
        return ncr(self.M, x) * ncr(self.N - self.M, self.n - x) / ncr(self.N, self.n)

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
