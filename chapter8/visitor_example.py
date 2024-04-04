from __future__ import annotations

from collections.abc import Callable
from typing import Protocol


class VisitorAcceptable(Protocol):
    def accept(self, visitor: Callable[[VisitorAcceptable], None]) -> None:
        ...


class Node:
    def accept(self, visitor: Callable[[VisitorAcceptable], None]) -> None:
        visitor(self)


class Branch(Node):
    def __init__(self, *args: Node) -> None:
        self.children = list(args)

    def accept(self, visitor: Callable[[VisitorAcceptable], None]) -> None:
        super().accept(visitor)

        for child in self.children:
            child.accept(visitor)


class ExampleVisitor:
    def __call__(self, acceptable: VisitorAcceptable) -> None:
        print(acceptable)


if __name__ == "__main__":
    left = Node()
    right = Node()
    branch = Branch(left, right)
    root = Branch(Node(), branch)

    root.accept(ExampleVisitor())
