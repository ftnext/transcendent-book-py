import contextlib
from collections.abc import Generator
from unittest import TestCase
from unittest.mock import MagicMock

from src.core import NumberConverter, ReplaceRuleInterface


@contextlib.contextmanager
def _create_mock_rule(
    expected_number: int, replacement: str
) -> Generator[ReplaceRuleInterface, None, None]:
    rule = MagicMock(spec=ReplaceRuleInterface)
    rule.replace.return_value = replacement
    yield rule
    rule.replace.assert_called_once_with(expected_number)


class NumberConverterTestCase(TestCase):
    def test_convert_with_empty_rules(self):
        fizz_buzz = NumberConverter([])
        self.assertEqual("", fizz_buzz.convert(1))

    def test_convert_with_single_rule(self):
        rule = MagicMock(spec=ReplaceRuleInterface)
        rule.replace.return_value = "Replaced"

        fizz_buzz = NumberConverter([rule])
        self.assertEqual("Replaced", fizz_buzz.convert(1))
        rule.replace.assert_called_once_with(1)

    def test_convert_with_fizz_buzz_rules(self):
        with _create_mock_rule(1, "Fizz") as fizz_rule, _create_mock_rule(
            1, "Buzz"
        ) as buzz_rule:
            fizz_buzz = NumberConverter([fizz_rule, buzz_rule])
            self.assertEqual("FizzBuzz", fizz_buzz.convert(1))
