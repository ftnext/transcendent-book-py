from typing import Protocol


class ReplaceRuleInterface(Protocol):
    def apply(self, carry: str, n: int) -> str:
        ...

    def match(self, carry: str, n: int) -> bool:
        ...
