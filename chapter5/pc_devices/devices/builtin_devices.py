from devices.operation import KeyboardInterface, PointerDeviceInterface


class BuiltinKeyboard(KeyboardInterface):
    def type_key(self, code: str) -> None:
        ...


class BuiltinTrackpad(PointerDeviceInterface):
    def move_cursor(self, direction: float, distance: float) -> None:
        ...
