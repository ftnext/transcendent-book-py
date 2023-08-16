from devices.connection import InternalBus, USBDeviceInterface
from devices.operation import KeyboardInterface, PointerDeviceInterface


class USBKeyboard(KeyboardInterface, USBDeviceInterface):
    def connect(self, bus: InternalBus) -> None:
        ...

    def type_key(self, code: str) -> None:
        ...


class USBMouse(PointerDeviceInterface, USBDeviceInterface):
    def connect(self, bus: InternalBus) -> None:
        ...

    def move_cursor(self, direction: float, distance: float) -> None:
        ...
