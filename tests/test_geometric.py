from unittest import TestCase

from pdlpy import Geometric


class TestGeometric(TestCase):
    def setUp(self):
        self.geometric = Geometric(1.0)

    def test_mean(self):
        self.assertEqual(1.0, self.geometric.mean)

    def test_var(self):
        self.assertEqual(0.0, self.geometric.var)

    def test_pmf(self):
        self.assertEqual(1.0, self.geometric.pmf(0))

    def test_cdf(self):
        self.assertEqual(1.0, self.geometric.cdf(0))
        self.assertEqual(1.0, self.geometric.cdf(1))
