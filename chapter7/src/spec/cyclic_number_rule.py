class CyclicNumberRule:
    def __init__(self, base: int, replacement: str) -> None:
        self.base = base
        self.replacement = replacement

    def apply(self, carry: str, n: int) -> str:
        return carry + self.replacement

    def match(self, carry: str, n: int) -> bool:
        return n % self.base == 0
