from unittest import TestCase

from src.core import NumberConverter


class NumberConverterTestCase(TestCase):
    def test_convert_with_empty_rules(self):
        fizz_buzz = NumberConverter([])
        self.assertEqual("", fizz_buzz.convert(1))
