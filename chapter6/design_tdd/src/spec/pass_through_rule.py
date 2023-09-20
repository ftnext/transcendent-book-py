class PassThroughRule:
    def apply(self, carry: str, n: int) -> str:
        return str(n)

    def match(self, carry: str, n: int) -> bool:
        return carry == ""
