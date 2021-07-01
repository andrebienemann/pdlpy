from unittest import TestCase

from pdlpy import Hypergeometric


class TestHypergeometric(TestCase):
    def setUp(self):
        self.hypergeometric = Hypergeometric(1, 2, 1)

    def test_str(self):
        self.assertEqual(
            "Hypergeometric(n=1, N=2, M=1, mean=0.5, var=0.25)",
            str(self.hypergeometric),
        )

    def test_mean(self):
        self.assertEqual(0.5, self.hypergeometric.mean)

    def test_var(self):
        self.assertEqual(0.25, self.hypergeometric.var)

    def test_pmf(self):
        self.assertEqual(0.5, self.hypergeometric.pmf(0))

    def test_cdf(self):
        self.assertEqual(0.5, self.hypergeometric.cdf(0))
        self.assertEqual(1.0, self.hypergeometric.cdf(1))
