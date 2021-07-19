class Distribution:
    def __init__(self, mean=0.0, var=0.0):
        self._mean = mean
        self._var = var

    @property
    def mean(self) -> float:
        return self._mean

    @property
    def var(self) -> float:
        return self._var
