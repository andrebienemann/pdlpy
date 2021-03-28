class Uniform:
    """
    Continuous distribution of a random variable X in interval [a; b] where any value of X has an equal probability
    """

    def __init__(self, a, b):
        """
        Paramters
        a: the minimum value of X
        b: the maximum value of X
        """
        self.a = a
        self.b = b
        self.mean = (a + b) / 2
        self.var = (b - a) ** 2 / 12

    def pdf(self, x):
        """
        Probability Density Function

        Paramters
        x: a value of random variable X

        Returns
        the relative likelihood that a value of X would lie in sample space
        """
        return 1 / (self.b - self.a)

    def cdf(self, x):
        """
        Cumulative Distribution Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value less than or equal to x
        """
        if x <= self.a:
            return 0.0
        elif x >= self.b:
            return 1.0
        else:
            return (x - self.a) / (self.b - self.a)
