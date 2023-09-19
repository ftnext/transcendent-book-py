from unittest import TestCase

from src.spec import CyclicNumberRule


class CyclicNumberRuleTestCase(TestCase):
    def test_replace(self):
        rule = CyclicNumberRule(3, "Fizz")
        self.assertEqual("", rule.replace(1))
        self.assertEqual("Fizz", rule.replace(3))
        self.assertEqual("Fizz", rule.replace(6))
