from pdlpy.distribution import Distribution


class Bernoulli(Distribution):
    """
    Discrete probability distribution of a random variable X which takes either value 1 or 0
    """

    def __init__(self, p: float):
        """
        Parameters
        p: the probability of positive outcome of an experiment
        """
        self._p = p
        self._mean = p
        self._var = p * (1 - p)

    def __str__(self):
        return (
            "Bernoulli("
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
        if x == 0:
            return 1.0 - self._p
        else:
            return self._p

    def cdf(self, x: int) -> float:
        """
        Cumulative Distribution Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value less than or equal to x
        """
        if x == 0:
            return 1.0 - self._p
        else:
            return 1.0
