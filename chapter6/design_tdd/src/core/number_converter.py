from collections.abc import Iterable

from src.core.replace_rule_interface import ReplaceRuleInterface


class NumberConverter:
    def __init__(self, rules: Iterable[ReplaceRuleInterface]) -> None:
        self.rules = rules

    def convert(self, n: int) -> str:
        result = ""
        for rule in self.rules:
            result += rule.replace(n)
        return result
