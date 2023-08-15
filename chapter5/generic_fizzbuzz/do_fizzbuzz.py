from fizzbuzz.core import NumberConverter
from fizzbuzz.spec import CyclicNumberRule, PassThroughRule

fizzbuzz_converter = NumberConverter(
    [
        CyclicNumberRule(3, "Fizz"),
        CyclicNumberRule(5, "Buzz"),
        PassThroughRule(),
    ]
)

assert fizzbuzz_converter.convert(1) == "1"
assert fizzbuzz_converter.convert(3) == "Fizz"
assert fizzbuzz_converter.convert(5) == "Buzz"
assert fizzbuzz_converter.convert(15) == "FizzBuzz"
