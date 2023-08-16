from db.interface import DataInputInterface, DataOutputInterface
from db.vendor import VendorDatabaseDriver


class CommandExecutor:
    def __init__(self, input: DataInputInterface) -> None:
        self.input = input

    def exec(self, *args):
        self.input.write(*args)


class QueryService:
    def __init__(self, output: DataOutputInterface) -> None:
        self.output = output

    def query(self, *args):
        self.output.read(*args)


if __name__ == "__main__":
    driver = VendorDatabaseDriver()
    # DatabaseInterfaceDriverからインスタンス化もできる
    executor = CommandExecutor(driver)
    service = QueryService(driver)
