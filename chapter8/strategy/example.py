from collections.abc import Sequence
from typing import Protocol


class ExpressionInterface(Protocol):
    def set_variables(self, variables: Sequence[float]) -> None:
        ...

    def evaluate(self) -> float:
        ...


class CalculationStrategyInterface(Protocol):
    def validate(self, variables: Sequence[float]) -> bool:
        ...

    def calculate(self, variables: Sequence[float]) -> float:
        ...


class Expression:
    def __init__(self) -> None:
        self.variables: Sequence[float] | None = None
        self.calculation_strategy: CalculationStrategyInterface | None = None

    def set_calculation_strategy(
        self, strategy: CalculationStrategyInterface
    ) -> None:
        self.calculation_strategy = strategy

    def set_variables(self, variables: Sequence[float]) -> None:
        if self.calculation_strategy is None:
            raise RuntimeError
        if not self.calculation_strategy.validate(variables):
            raise ValueError
        self.variables = variables

    def evaluate(self) -> float:
        if self.variables is None or self.calculation_strategy is None:
            raise RuntimeError
        return self.calculation_strategy.calculate(self.variables)


class PlusCalculationStrategy:
    def validate(self, variables: Sequence[float]) -> bool:
        return len(variables) == 2

    def calculate(self, variables: Sequence[float]) -> float:
        return variables[0] + variables[1]


if __name__ == "__main__":
    expression = Expression()
    expression.set_calculation_strategy(PlusCalculationStrategy())

    expression.set_variables([1.1, 2.2])
    print(expression.evaluate())  # 3.3000000000000003
