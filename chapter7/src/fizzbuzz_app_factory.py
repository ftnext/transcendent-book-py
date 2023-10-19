from src.app import FizzBuzzSequencePrinter, OutputInterface
from src.core import NumberConverter, ReplaceRuleInterface
from src.spec import CyclicNumberRule, PassThroughRule


class FizzBuzzAppFactory:
    def create(self) -> FizzBuzzSequencePrinter:
        return FizzBuzzSequencePrinter(
            self.create_fizzbuzz(), self.create_output()
        )

    def create_fizzbuzz(self) -> NumberConverter:
        return NumberConverter(
            [
                self.create_fizz_rule(),
                self.create_buzz_rule(),
                self.create_pass_through_rule(),
            ]
        )

    def create_fizz_rule(self) -> ReplaceRuleInterface:
        return CyclicNumberRule(3, "Fizz")

    def create_buzz_rule(self) -> ReplaceRuleInterface:
        return CyclicNumberRule(5, "Buzz")

    def create_pass_through_rule(self) -> ReplaceRuleInterface:
        return PassThroughRule()

    def create_output(self) -> OutputInterface:
        return ConsoleOutput()


class ConsoleOutput:
    def write(self, data: str) -> None:
        print(data, end="")
