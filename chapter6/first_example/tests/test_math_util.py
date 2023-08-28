from unittest import TestCase

from src.math_util import MathUtil


class SaturateTestCase(TestCase):
    def test_範囲内ならそのまま(self) -> None:
        # ここでは範囲を [1, 3] としている
        math_util = MathUtil()
        self.assertEqual(2, math_util.saturate(2, 1, 3))

    def test_範囲外なら上限値または下限値になる(self) -> None:
        # ここでは範囲を [1, 3] としている
        math_util = MathUtil()
        self.assertEqual(1, math_util.saturate(0, 1, 3))
        self.assertEqual(3, math_util.saturate(4, 1, 3))

    def test_上限値または下限値と同じ値は範囲内(self) -> None:
        math_util = MathUtil()
        self.assertEqual(1, math_util.saturate(1, 1, 3))
        self.assertEqual(3, math_util.saturate(3, 1, 3))
