import sys
from unittest import TestCase

from src.math import Math

int_min = -sys.maxsize - 1


class MathTest(TestCase):
    def test_min(self) -> None:
        math = Math()
        self.assertEqual(0, math.min(0, 1))
        self.assertEqual(0, math.min(1, 0))
        self.assertEqual(-1, math.min(0, -1))
        self.assertEqual(-1, math.min(-1, 0))
        self.assertEqual(0, math.min(0, 0))
        self.assertEqual(0, math.min(0, sys.maxsize))
        self.assertEqual(int_min, math.min(0, int_min))

    def test_max(self) -> None:
        math = Math()
        self.assertEqual(1, math.max(0, 1))
        self.assertEqual(1, math.max(1, 0))
        self.assertEqual(0, math.max(0, -1))
        self.assertEqual(0, math.max(-1, 0))
        self.assertEqual(0, math.max(0, 0))
        self.assertEqual(sys.maxsize, math.max(0, sys.maxsize))
        self.assertEqual(0, math.max(0, int_min))
