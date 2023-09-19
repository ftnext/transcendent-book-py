from typing import Protocol


class ReplaceRuleInterface(Protocol):
    def replace(self, n: int) -> str:
        ...
