from unittest import TestCase
from unittest.mock import MagicMock

from src.core import NumberConverter, ReplaceRuleInterface


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
