from fizzbuzz.core import ReplaceRuleInterface


class CyclicNumberRule(ReplaceRuleInterface):
    """倍数に関するルール"""

    def __init__(self, base: int, replacement: str) -> None:
        self.base = base
        self.replacement = replacement

    def match(self, carry: str, n: int) -> bool:
        return n % self.base == 0

    def apply(self, carry: str, n: int) -> str:
        return carry + self.replacement


class PassThroughRule(ReplaceRuleInterface):
    def match(self, carry: str, n: int) -> bool:
        return carry == ""

    def apply(self, carry: str, n: int) -> str:
        return str(n)
