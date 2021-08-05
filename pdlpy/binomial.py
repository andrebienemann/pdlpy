from pdlpy.distribution import Distribution
from pdlpy.math import ncr


class Binomial(Distribution):
    """
    Discrete probability distribution of a number of successes in a sequence of independent experiments
    """

    def __init__(self, n: int, p: float):
        """
        Parameters
        n: the size of the sequence
        p: the probability of success
        """
        self._n = n
        self._p = p
        self._mean = n * p
        self._var = n * p * (1 - p)

    def __str__(self):
        return (
            "Binomial("
            f"n={self._n}, "
            f"p={self._p:.2f}, "
            f"mean={self._mean:.2f}, "
            f"var={self._var:.2f}"
            ")"
        )

    def pmf(self, x: int) -> float:
        """
        Probability Mass Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value exactly equal to x
        """
        return ncr(self._n, x) * self._p ** x * (1 - self._p) ** (self._n - x)

    def cdf(self, x: int) -> float:
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
