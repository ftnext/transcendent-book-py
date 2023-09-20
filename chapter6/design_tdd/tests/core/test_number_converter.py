import contextlib
from collections.abc import Generator
from unittest import TestCase
from unittest.mock import MagicMock

from src.core import NumberConverter, ReplaceRuleInterface


@contextlib.contextmanager
def _create_matched_mock_rule(
    expected_number: int,
    expected_carry: str,
    replacement: str,
) -> Generator[ReplaceRuleInterface, None, None]:
    rule = MagicMock(spec=ReplaceRuleInterface)
    rule.match.return_value = True
    rule.apply.return_value = replacement
    yield rule
    rule.match.assert_called_once_with(expected_carry, expected_number)
    rule.apply.assert_called_once_with(expected_carry, expected_number)


@contextlib.contextmanager
def _create_unmatched_mock_rule(
    expected_number: int,
    expected_carry: str,
) -> Generator[ReplaceRuleInterface, None, None]:
    rule = MagicMock(spec=ReplaceRuleInterface)
    rule.match.return_value = False
    yield rule
    rule.match.assert_called_once_with(expected_carry, expected_number)
    rule.apply.assert_not_called()


class NumberConverterTestCase(TestCase):
    def test_convert_with_empty_rules(self):
        fizz_buzz = NumberConverter([])
        self.assertEqual("", fizz_buzz.convert(1))

    def test_convert_with_single_rule(self):
        with _create_matched_mock_rule(1, "", "Replaced") as rule:
            fizz_buzz = NumberConverter([rule])
            self.assertEqual("Replaced", fizz_buzz.convert(1))

    def test_convert_compositing_rule_results(self):
        with _create_matched_mock_rule(
            1, "", "Fizz"
        ) as fizz_rule, _create_matched_mock_rule(
            1, "Fizz", "FizzBuzz"
        ) as buzz_rule:
            fizz_buzz = NumberConverter([fizz_rule, buzz_rule])
            self.assertEqual("FizzBuzz", fizz_buzz.convert(1))

    def test_convert_skipping_unmatched_rules(self):
        with _create_unmatched_mock_rule(
            1, ""
        ) as fizz_rule, _create_unmatched_mock_rule(
            1, ""
        ) as buzz_rule, _create_matched_mock_rule(
            1, "", "1"
        ) as constant_rule:
            fizz_buzz = NumberConverter([fizz_rule, buzz_rule, constant_rule])
            self.assertEqual("1", fizz_buzz.convert(1))
