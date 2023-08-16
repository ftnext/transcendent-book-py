import math
from collections.abc import Iterable

from devices.builtin_devices import BuiltinKeyboard, BuiltinTrackpad
from devices.external_devices import USBKeyboard, USBMouse
from devices.operation import KeyboardInterface, PointerDeviceInterface


class PCOperator:
    def __init__(
        self,
        keyboard: KeyboardInterface,
        pointer_device: PointerDeviceInterface,
    ) -> None:
        self.keyboard = keyboard
        self.pointer_device = pointer_device

    def input_text(self, codes: Iterable[str]) -> None:
        for code in codes:
            self.keyboard.type_key(code)

    def point_at(self, x: int, y: int) -> None:
        direction = x / y
        distance = math.sqrt(x**2 + y**2)
        self.pointer_device.move_cursor(direction, distance)


if __name__ == "__main__":
    # デバイスを付け替えできる（USB接続の使い方はここでは見ていない）
    operator1 = PCOperator(BuiltinKeyboard(), BuiltinTrackpad())
    operator2 = PCOperator(BuiltinKeyboard(), USBMouse())
    operator3 = PCOperator(USBKeyboard(), USBMouse())
