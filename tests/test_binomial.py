from unittest import TestCase

from pdlpy import Binomial


class TestBinomial(TestCase):
    def setUp(self):
        self.binomial = Binomial(1, 0.0)

    def test_str(self):
        self.assertEqual(
            "Binomial(n=1, p=0.00, mean=0.00, var=0.00)",
            str(self.binomial),
        )

    def test_mean(self):
        self.assertEqual(0.0, self.binomial.mean)

    def test_var(self):
        self.assertEqual(0.0, self.binomial.var)

    def test_pdf(self):
        self.assertEqual(1.0, self.binomial.pmf(0))

    def test_cdf(self):
        self.assertEqual(1.0, self.binomial.cdf(0))
        self.assertEqual(1.0, self.binomial.cdf(1))
