import sys
from typing import Protocol


class LoggerInterface(Protocol):
    def log(self, message: str) -> None:
        ...


class PetShop:
    def __init__(self, logger: LoggerInterface) -> None:
        self.logger = logger

    def paycheck(self) -> None:
        self.logger.log("begin")
        print("transaction処理 ...")
        self.logger.log("end")


class NullLogger:
    def log(self, message: str) -> None:
        pass


class Logger:
    def log(self, message: str) -> None:
        print(message, file=sys.stderr)


if __name__ == "__main__":
    shop = PetShop(NullLogger())
    shop.paycheck()

"""
% python polymorphism_logger.py
transaction処理 ...

NullLoggerをLoggerに差し替えた場合
% python polymorphism_logger.py
begin
transaction処理 ...
end
"""
