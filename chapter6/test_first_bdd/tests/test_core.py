from unittest import TestCase

from src.core import NumberConverter


class NumberConverterTestCase(TestCase):
    def test_convert(self):
        fizz_buzz = NumberConverter()

        self.assertEqual("1", fizz_buzz.convert(1))
        self.assertEqual("2", fizz_buzz.convert(2))
        self.assertEqual("Fizz", fizz_buzz.convert(3))
        self.assertEqual("4", fizz_buzz.convert(4))
        self.assertEqual("Buzz", fizz_buzz.convert(5))
