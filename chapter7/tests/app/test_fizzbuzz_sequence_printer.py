from unittest import TestCase
from unittest.mock import MagicMock, call

from src.app import FizzBuzzSequencePrinter, OutputInterface
from src.core import NumberConverter


class FizzBuzzSequencePrinterTestCase(TestCase):
    def test_print_none(self):
        converter = MagicMock(spec=NumberConverter)
        output = MagicMock(spec=OutputInterface)
        printer = FizzBuzzSequencePrinter(converter, output)

        printer.print_range(0, -1)

        converter.convert.assert_not_called()
        output.write.assert_not_called()

    def test_print_1_to_3(self):
        converter = MagicMock(spec=NumberConverter)
        converter.convert.side_effect = ["1", "2", "Fizz"]
        output = MagicMock(spec=OutputInterface)
        printer = FizzBuzzSequencePrinter(converter, output)

        printer.print_range(1, 3)

        converter.convert.assert_has_calls([call(1), call(2), call(3)])
        output.write.assert_has_calls(
            [call("1 1\n"), call("2 2\n"), call("3 Fizz\n")]
        )
