from unittest import TestCase

from pdlpy import Exponential


class TestExponential(TestCase):
    def setUp(self):
        self.exponential = Exponential(1.0)

    def test_mean(self):
        self.assertEqual(1.0, self.exponential.mean)

    def test_var(self):
        self.assertEqual(1.0, self.exponential.var)

    def test_pdf(self):
        self.assertEqual(1.0, self.exponential.pdf(0))

    def test_cdf(self):
        self.assertEqual(0.0, self.exponential.cdf(0))
