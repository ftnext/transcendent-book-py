from abc import ABCMeta, abstractmethod


class DataInputInterface(metaclass=ABCMeta):
    @abstractmethod
    def write(self, key: str, data) -> None:
        ...


class DataOutputInterface(metaclass=ABCMeta):
    @abstractmethod
    def read(self, key: str):
        ...


class DatabaseDriverInterface(DataInputInterface, DataOutputInterface):
    ...
