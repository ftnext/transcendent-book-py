"""PYTHONPATH=$PWD python src/__main__.py"""

from src.fizzbuzz_app_factory import FizzBuzzAppFactory


class App:
    @staticmethod
    def main() -> None:
        factory = FizzBuzzAppFactory()
        printer = factory.create()
        printer.print_range(1, 100)


App.main()
