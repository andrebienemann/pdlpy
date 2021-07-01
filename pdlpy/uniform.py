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
        self.__a = a
        self.__b = b
        self.__mean = (a + b) / 2
        self.__var = (b - a) ** 2 / 12

    @property
    def mean(self):
        return self.__mean

    @property
    def var(self):
        return self.__var

    def pdf(self, x=None):
        """
        Probability Density Function

        Paramters
        x: a value of random variable X

        Returns
        the relative likelihood that a value of X would lie in sample space
        """
        return 1 / (self.__b - self.__a)

    def cdf(self, x):
        """
        Cumulative Distribution Function

        Parameters
        x: a value of the random variable X

        Returns
        the probability that X will take a value less than or equal to x
        """
        if x <= self.__a:
            return 0.0
        elif x >= self.__b:
            return 1.0
        else:
            return (x - self.__a) / (self.__b - self.__a)
