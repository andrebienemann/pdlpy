from unittest import TestCase

from pdlpy import Poisson


class TestPoisson(TestCase):
    def setUp(self):
        self.poisson = Poisson(0.0)

    def test_mean(self):
        self.assertEqual(0.0, self.poisson.mean)

    def test_var(self):
        self.assertEqual(0.0, self.poisson.var)

    def test_pmf(self):
        self.assertEqual(1.0, self.poisson.pmf(0))

    def test_cdf(self):
        self.assertEqual(1.0, self.poisson.cdf(0))
        self.assertEqual(1.0, self.poisson.cdf(1))
