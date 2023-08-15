from abc import ABCMeta, abstractmethod
from collections.abc import Iterable


class ReplaceRuleInterface(metaclass=ABCMeta):
    @abstractmethod
    def match(self, carry: str, n: int) -> bool:
        ...

    @abstractmethod
    def apply(self, carry: str, n: int) -> str:
        ...


class NumberConverter:
    def __init__(self, rules: Iterable[ReplaceRuleInterface]) -> None:
        self.rules = list(rules)

    def convert(self, n: int) -> str:
        carry = ""
        for rule in self.rules:
            if rule.match(carry, n):
                carry = rule.apply(carry, n)
        return carry
