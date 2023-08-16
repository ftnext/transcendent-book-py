from abc import ABCMeta, abstractmethod


class KeyboardInterface(metaclass=ABCMeta):
    @abstractmethod
    def type_key(self, code: str) -> None:
        ...


class PointerDeviceInterface(metaclass=ABCMeta):
    @abstractmethod
    def move_cursor(self, direction: float, distance: float) -> None:
        ...
