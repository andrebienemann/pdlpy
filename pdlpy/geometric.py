class Geometric:
    """
    Discrete probability distributions of the random number X of Bernoulli trials needed to get a single success
    """

    def __init__(self, p):
        """
        Parameters
        p: the probability of the positive outcome of the experiment
        """
        self.__p = p
        self.__mean = 1 / p
        self.__var = (1 - p) / (p ** 2)

    def __str__(self):
        p = round(self.__p, 2)
        mean = round(self.__mean, 2)
        var = round(self.__var, 2)
        return f"Geometric(p={p}, mean={mean}, var={var})"

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
        return (1 - self.__p) ** x * self.__p

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
