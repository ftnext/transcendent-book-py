import contextlib
from collections.abc import Generator
from unittest import TestCase
from unittest.mock import MagicMock

from src.core import NumberConverter, ReplaceRuleInterface


@contextlib.contextmanager
def _create_mock_rule(
    expected_number: int,
    expected_carry: str,
    match_result: bool,
    replacement: str,
) -> Generator[ReplaceRuleInterface, None, None]:
    rule = MagicMock(spec=ReplaceRuleInterface)
    rule.apply.return_value = replacement
    rule.match.return_value = match_result
    yield rule
    rule.match.assert_called_once_with(expected_carry, expected_number)


class NumberConverterTestCase(TestCase):
    def test_convert_with_empty_rules(self):
        fizz_buzz = NumberConverter([])
        self.assertEqual("", fizz_buzz.convert(1))

    def test_convert_with_single_rule(self):
        with _create_mock_rule(1, "", True, "Replaced") as rule:
            fizz_buzz = NumberConverter([rule])
            self.assertEqual("Replaced", fizz_buzz.convert(1))
            rule.apply.assert_called_once_with("", 1)

    def test_convert_compositing_rule_results(self):
        with _create_mock_rule(
            1, "", True, "Fizz"
        ) as fizz_rule, _create_mock_rule(
            1, "Fizz", True, "FizzBuzz"
        ) as buzz_rule:
            fizz_buzz = NumberConverter([fizz_rule, buzz_rule])
            self.assertEqual("FizzBuzz", fizz_buzz.convert(1))
            fizz_rule.apply.assert_called_once_with("", 1)
            buzz_rule.apply.assert_called_once_with("Fizz", 1)

    def test_convert_skipping_unmatched_rules(self):
        with _create_mock_rule(
            1, "", False, "Fizz"
        ) as fizz_rule, _create_mock_rule(
            1, "", False, "Buzz"
        ) as buzz_rule, _create_mock_rule(
            1, "", True, "1"
        ) as constant_rule:
            fizz_buzz = NumberConverter([fizz_rule, buzz_rule, constant_rule])
            self.assertEqual("1", fizz_buzz.convert(1))
            fizz_rule.apply.assert_not_called()
            buzz_rule.apply.assert_not_called()
            constant_rule.apply.assert_called_once_with("", 1)
