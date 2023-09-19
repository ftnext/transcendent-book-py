from unittest import TestCase

from src.spec import PassThroughRule


class PassThroughRuleTestCase(TestCase):
    def test_replace(self):
        rule = PassThroughRule()
        self.assertEqual("1", rule.replace(1))
