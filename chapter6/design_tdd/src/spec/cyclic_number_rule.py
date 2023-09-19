class CyclicNumberRule:
    def __init__(self, base: int, replacement: str) -> None:
        self.base = base
        self.replacement = replacement

    def replace(self, n: int) -> str:
        return self.replacement if n % self.base == 0 else ""
