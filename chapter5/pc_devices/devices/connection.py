from abc import ABCMeta, abstractmethod


class InternalBus:
    ...


class USBDeviceInterface(metaclass=ABCMeta):
    @abstractmethod
    def connect(self, bus: InternalBus) -> None:
        ...


class USBPort:
    def __init__(self, internal_bus: InternalBus) -> None:
        self._internal_bus = internal_bus

    def plug(self, device: USBDeviceInterface) -> None:
        device.connect(self._internal_bus)
