from db.interface import DatabaseDriverInterface


class VendorDatabaseDriver(DatabaseDriverInterface):
    def write(self, key: str, data) -> None:
        ...

    def read(self, key: str):
        ...
