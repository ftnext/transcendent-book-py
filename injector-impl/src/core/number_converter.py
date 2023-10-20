from collections.abc import Iterable

from injector import inject

from src.core.replace_rule_interface import ReplaceRuleInterface


class NumberConverter:
    @inject
    def __init__(self, rules: Iterable[ReplaceRuleInterface]) -> None:
        self.rules = rules

    def convert(self, n: int) -> str:
        carry = ""
        for rule in self.rules:
            if rule.match(carry, n):
                carry = rule.apply(carry, n)
        return carry
