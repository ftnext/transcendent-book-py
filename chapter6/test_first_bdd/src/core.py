class NumberConverter:
    def convert(self, n: int) -> str:
        if n == 3:
            return "Fizz"
        if n == 5:
            return "Buzz"
        return str(n)
