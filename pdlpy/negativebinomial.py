from pdlpy import binomial

class Negativebinomial:
    """
    Discrete probability distribution of the number of trials needed to get r successes
    """

    def __init__(self, r, p):
        """
        Parameters
        r: the number of successes
        p: the probability of success
        """
        self.r = r
        self.p = p
        self.mean = r / p
        self.var = r / p ** 2

    def pmf(self, x):
        """
        Probability Mass Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value exactly equal to x
        """
        return (
            binomial(x - 1, self.r - 1)
            * (self.p ** self.r)
            * ((1 - self.p) ** (x - self.r))
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
