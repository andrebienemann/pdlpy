"""
Probability Distribution Library for Python
"""

import math

__version__ = "0.1.0.rc1"


def binomial(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

from .bernoulli import Bernoulli
from .binomial import Binomial
from .exponential import Exponential
from .geometric import Geometric
from .hypergeometric import Hypergeometric
from .negativebinomial import Negativebinomial
from .normal import Normal
from .poisson import Poisson
from .uniform import Uniform
