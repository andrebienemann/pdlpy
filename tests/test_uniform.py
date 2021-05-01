from unittest import TestCase

from pdlpy import Uniform


class TestUniform(TestCase):
    def setUp(self):
        self.uniform = Uniform(0.0, 1.0)

    def test_mean(self):
        self.assertEqual(0.5, self.uniform.mean)

    def test_var(self):
        self.assertEqual(0.08, round(self.uniform.var, 2))

    def test_pdf(self):
        self.assertEqual(1.0, self.uniform.pdf(1.0))

    def test_cdf(self):
        self.assertEqual(0.0, self.uniform.cdf(0.0))
        self.assertEqual(0.5, self.uniform.cdf(0.5))
        self.assertEqual(1.0, self.uniform.cdf(1.0))
