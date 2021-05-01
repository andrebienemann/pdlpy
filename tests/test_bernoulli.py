from unittest import TestCase

from pdlpy import Bernoulli


class TestBernoulli(TestCase):
    def setUp(self):
        self.bernoulli = Bernoulli(0.0)

    def test_mean(self):
        self.assertEqual(0.0, self.bernoulli.mean)

    def test_var(self):
        self.assertEqual(0.0, self.bernoulli.var)

    def test_pmf(self):
        self.assertEqual(0.0, self.bernoulli.pmf(1))
        self.assertEqual(1.0, self.bernoulli.pmf(0))

    def test_cdf(self):
        self.assertEqual(1.0, self.bernoulli.cdf(1))
        self.assertEqual(1.0, self.bernoulli.cdf(0))
