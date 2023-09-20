from unittest import TestCase

from src.spec import PassThroughRule


class PassThroughRuleTestCase(TestCase):
    def test_apply(self):
        rule = PassThroughRule()
        self.assertEqual("1", rule.apply("", 1))
        self.assertEqual("2", rule.apply("", 2))
        # applyは無条件に適用される（NumberConverterでFizz3にならないように制御）
        self.assertEqual("3", rule.apply("Fizz", 3))

    def test_match(self):
        rule = PassThroughRule()
        self.assertTrue(rule.match("", 0))
        self.assertFalse(rule.match("Fizz", 0))
