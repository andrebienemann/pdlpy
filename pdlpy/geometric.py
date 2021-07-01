from pdlpy.distribution import Distribution


class Geometric(Distribution):
    """
    Discrete probability distributions of the random number X of Bernoulli trials needed to get a single success
    """

    def __init__(self, p):
        """
        Parameters
        p: the probability of the positive outcome of the experiment
        """
        self._p = p
        self._mean = 1 / p
        self._var = (1 - p) / (p ** 2)

    def __str__(self):
        p = round(self._p, 2)
        mean = round(self._mean, 2)
        var = round(self._var, 2)
        return f"Geometric(p={p}, mean={mean}, var={var})"

    def pmf(self, x):
        """
        Probability Mass Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value exactly equal to x
        """
        return (1 - self._p) ** x * self._p

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
