class Geometric:
    """
    Discrete probability distributions of the random number X of Bernoulli trials needed to get a single success
    """

    def __init__(self, p):
        """
        Parameters
        p: the probability of the positive outcome of the experiment
        """
        self.p = p
        self.mean = 1 / p
        self.var = (1 - p) / (p ** 2)

    def pmf(self, x):
        """
        Probability Mass Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value exactly equal to x
        """
        return (1 - self.p) ** x * self.p

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
