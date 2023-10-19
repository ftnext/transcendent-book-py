from unittest import TestCase

from src.spec import CyclicNumberRule


class CyclicNumberRuleTestCase(TestCase):
    def test_apply(self):
        rule = CyclicNumberRule(0, "Buzz")
        self.assertEqual("Buzz", rule.apply("", 0))
        self.assertEqual("FizzBuzz", rule.apply("Fizz", 0))

    def test_match(self):
        rule = CyclicNumberRule(3, "")
        self.assertFalse(rule.match("", 1))
        self.assertTrue(rule.match("", 3))
        self.assertTrue(rule.match("", 6))
