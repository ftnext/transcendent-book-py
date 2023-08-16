from abc import ABCMeta, abstractmethod


class DatabaseDriverInterface(metaclass=ABCMeta):
    @abstractmethod
    def write(self, key: str, data) -> None:
        ...

    @abstractmethod
    def read(self, key: str):
        ...


class DatabaseDriverVer1(DatabaseDriverInterface):
    def write(self, key: str, data) -> None:
        ...

    def read(self, key: str):
        ...


class DatabaseDriverVer2(DatabaseDriverInterface):
    def write(self, key: str, data) -> None:
        ...

    def read(self, key: str):
        ...
