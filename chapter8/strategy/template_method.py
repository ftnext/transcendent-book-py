from abc import ABCMeta, abstractmethod
from collections.abc import Sequence
from typing import Protocol, cast


class ExpressionInterface(Protocol):
    def set_variables(self, variables: Sequence[float]) -> None:
        ...

    def evaluate(self) -> float:
        ...


class AbstractExpression(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.variables: Sequence[float] | None = None

    def set_variables(self, variables: Sequence[float]) -> None:
        if not self.validate(variables):
            raise ValueError
        self.variables = variables

    def evaluate(self) -> float:
        if self.variables is None:
            raise RuntimeError
        return self.calculate()

    @abstractmethod
    def validate(self, variables: Sequence[float]) -> bool:
        raise NotImplementedError

    @abstractmethod
    def calculate(self) -> float:
        raise NotImplementedError


class PlusExpression(AbstractExpression):
    # validateは属性に設定する前の検証なので引数を持つ
    def validate(self, variables: Sequence[float]) -> bool:
        return len(variables) == 2

    # calculateは属性に設定されたvariablesを使えるので引数を持たない
    def calculate(self) -> float:
        variables = cast(Sequence[float], self.variables)
        return variables[0] + variables[1]


if __name__ == "__main__":
    expression = PlusExpression()

    expression.set_variables([1.1, 2.2])
    print(expression.evaluate())
