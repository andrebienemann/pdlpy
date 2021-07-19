from unittest import TestCase

from pdlpy.distribution import Distribution


class TestDistribution(TestCase):
    def setUp(self):
        self.binomial = Distribution(0.0, 0.0)

    def test_mean(self):
        self.assertEqual(0.0, self.binomial.mean)

    def test_var(self):
        self.assertEqual(0.0, self.binomial.var)
