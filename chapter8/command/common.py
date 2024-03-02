from typing import Protocol


class CommandInterface(Protocol):
    def invoke(self) -> None:
        ...
