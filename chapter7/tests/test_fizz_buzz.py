"""FizzBuzz全体の振る舞いに対するBDD的なテスト"""

from unittest import TestCase

from src.core import NumberConverter
from src.spec import CyclicNumberRule, PassThroughRule


class FizzBuzzTestCase(TestCase):
    def test_fizz_buzz(self):
        fizz_buzz = NumberConverter(
            [
                CyclicNumberRule(3, "Fizz"),
                CyclicNumberRule(5, "Buzz"),
                PassThroughRule(),
            ]
        )
        self.assertEqual("1", fizz_buzz.convert(1))
        self.assertEqual("2", fizz_buzz.convert(2))
        self.assertEqual("Fizz", fizz_buzz.convert(3))
