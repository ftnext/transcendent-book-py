from typing import ABCMeta, abstractmethod

from injector import inject

from src.core import NumberConverter


class OutputInterface(metaclass=ABCMeta):
    @abstractmethod
    def write(self, data: str) -> None:
        raise NotImplementedError


class FizzBuzzSequencePrinter:
    @inject
    def __init__(
        self, fizzbuzz: NumberConverter, output: OutputInterface
    ) -> None:
        self.fizzbuzz = fizzbuzz
        self.output = output

    def print_range(self, begin: int, end: int) -> None:
        for i in range(begin, end + 1):
            text = self.fizzbuzz.convert(i)
            formatted_text = f"{i} {text}\n"
            self.output.write(formatted_text)
