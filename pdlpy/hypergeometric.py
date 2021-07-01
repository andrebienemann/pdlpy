from pdlpy.combinatorics import ncr
from pdlpy.distribution import Distribution


class Hypergeometric(Distribution):
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
        self._n = n
        self._N = N
        self._M = M
        self._mean = n * M / N
        self._var = n * M / N * (1 - M / N) * (N - n) / (N - 1)

    def __str__(self):
        n = round(self._n, 2)
        N = round(self._N, 2)
        M = round(self._M, 2)
        mean = round(self._mean, 2)
        var = round(self._var, 2)
        return f"Hypergeometric(n={n}, N={N}, M={M}, mean={mean}, var={var})"

    def pmf(self, x):
        """
        Probability Mass Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value exactly equal to x
        """
        return (
            ncr(self._M, x)
            * ncr(self._N - self._M, self._n - x)
            / ncr(self._N, self._n)
        )

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
