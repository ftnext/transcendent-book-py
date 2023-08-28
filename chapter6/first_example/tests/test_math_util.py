from unittest import TestCase
from unittest.mock import MagicMock

from src.math import Math
from src.math_util import MathUtil, MathUtilV2


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


class WithMockSaturateTestCase(TestCase):
    def test_saturate(self) -> None:
        math = MagicMock(spec=Math)
        math_util = MathUtilV2(math)

        math.max.return_value = 2
        math.min.return_value = 2

        result = math_util.saturate(2, 1, 3)

        self.assertEqual(2, result)
        math.max.assert_called_once_with(2, 1)
        math.min.assert_called_once_with(2, 3)
