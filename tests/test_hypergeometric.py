from unittest import TestCase

from pdlpy import Hypergeometric


class TestHypergeometric(TestCase):
    def setUp(self):
        self.hypergeometric = Hypergeometric(0, 2, 0)

    def test_mean(self):
        self.assertEqual(0.0, self.hypergeometric.mean)

    def test_var(self):
        self.assertEqual(0.0, self.hypergeometric.var)

    def test_pmf(self):
        self.assertEqual(1.0, self.hypergeometric.pmf(0))

    def test_cdf(self):
        self.assertEqual(1.0, self.hypergeometric.cdf(0))
