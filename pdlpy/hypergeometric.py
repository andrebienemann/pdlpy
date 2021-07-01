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
        self.__n = n
        self.__N = N
        self.__M = M
        self.__mean = n * M / N
        self.__var = n * M / N * (1 - M / N) * (N - n) / (N - 1)

    def __str__(self):
        n = round(self.__n, 2)
        N = round(self.__N, 2)
        M = round(self.__M, 2)
        mean = round(self.__mean, 2)
        var = round(self.__var, 2)
        return f"Hypergeometric(n={n}, N={N}, M={M}, mean={mean}, var={var})"

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
        return (
            ncr(self.__M, x)
            * ncr(self.__N - self.__M, self.__n - x)
            / ncr(self.__N, self.__n)
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
