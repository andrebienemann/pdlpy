class Bernoulli:
    """
    Discrete probability distribution of a random variable X which takes either value 1 or 0
    """

    def __init__(self, p):
        """
        Parameters
        p: the probability of positive outcome of an experiment
        """
        self.p = p
        self.mean = p
        self.var = p * (1 - p)

    def pmf(self, x):
        """
        Probability Mass Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value exactly equal to x
        """
        if x == 0:
            return 1.0 - self.p
        else:
            return self.p

    def cdf(self, x):
        """
        Cumulative Distribution Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value less than or equal to x
        """
        if x == 0:
            return 1.0 - self.p
        else:
            return 1.0
