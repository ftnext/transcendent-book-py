from unittest import TestCase

from src.core import NumberConverter


class NumberConverterTestCase(TestCase):
    def test_convert(self):
        fizz_buzz = NumberConverter()

        self.assertEqual("1", fizz_buzz.convert(1))
        self.assertEqual("2", fizz_buzz.convert(2))
