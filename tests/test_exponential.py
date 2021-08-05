from unittest import TestCase

from pdlpy import Exponential


class TestExponential(TestCase):
    def setUp(self):
        self.exponential = Exponential(1.0)

    def test_str(self):
        self.assertEqual(
            "Exponential(rate=1.00, mean=1.00, var=1.00)",
            str(self.exponential),
        )

    def test_mean(self):
        self.assertEqual(1.0, self.exponential.mean)

    def test_var(self):
        self.assertEqual(1.0, self.exponential.var)

    def test_pdf(self):
        self.assertEqual(1.0, self.exponential.pdf(0))

    def test_cdf(self):
        self.assertEqual(0.0, self.exponential.cdf(0))
