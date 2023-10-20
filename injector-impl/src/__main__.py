"""PYTHONPATH=$PWD python src/__main__.py"""

from collections.abc import Iterable

from injector import Injector, Module, multiprovider

from src.app import FizzBuzzSequencePrinter
from src.app.fizzbuzz_sequence_printer import OutputInterface
from src.core.replace_rule_interface import ReplaceRuleInterface
from src.spec import CyclicNumberRule, PassThroughRule


class ConsoleOutput(OutputInterface):
    def write(self, data: str) -> None:
        print(data, end="")


class FizzBuzzAppModule(Module):
    @multiprovider
    def provide_output_interface(self) -> Iterable[ReplaceRuleInterface]:
        return [
            CyclicNumberRule(3, "Fizz"),
            CyclicNumberRule(5, "Buzz"),
            PassThroughRule(),
        ]


def configure_output(binder):
    binder.bind(OutputInterface, to=ConsoleOutput())


injector = Injector([FizzBuzzAppModule, configure_output])
printer = injector.get(FizzBuzzSequencePrinter)
printer.print_range(1, 100)
