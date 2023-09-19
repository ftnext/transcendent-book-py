from collections.abc import Iterable

from src.core.replace_rule_interface import ReplaceRuleInterface


class NumberConverter:
    def __init__(self, rules: Iterable[ReplaceRuleInterface]) -> None:
        self.rules = rules
