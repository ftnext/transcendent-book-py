from src.math import Math


class MathUtil:
    def saturate(self, value: int, min_value: int, max_value: int) -> int:
        math = Math()
        return math.min(math.max(value, min_value), max_value)


class MathUtilV2:
    def __init__(self, math: Math) -> None:
        self.math = math

    def saturate(self, value: int, min_value: int, max_value: int) -> int:
        return self.math.min(self.math.max(value, min_value), max_value)
