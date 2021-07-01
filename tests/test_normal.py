from unittest import TestCase

from pdlpy import Normal


class TestNormal(TestCase):
    def setUp(self):
        self.normal = Normal(0.0, 1.0)

    def test_str(self):
        self.assertEqual("Normal(mean=0.0, var=1.0)", str(self.normal))

    def test_mean(self):
        self.assertEqual(0.0, self.normal.mean)

    def test_var(self):
        self.assertEqual(1.0, self.normal.var)

    def test_pdf(self):
        self.assertEqual(0.4, round(self.normal.pdf(0), 1))

    def test_cdf(self):
        self.assertEqual(0.5, self.normal.cdf(0))
