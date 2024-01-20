from typing import Protocol


class Runnable(Protocol):
    def run(self) -> None:
        ...


# 無名クラスに近いのはtypeだが、記述量が減らないのでクラス定義した
class ExampleRunnable:
    def __init__(self, value: str) -> None:
        self.value = value

    def run(self) -> None:
        print(self.value)


foo = "Foo"
runnable_object = ExampleRunnable(foo)
runnable_object.run()


def function_object() -> None:
    print(foo)  # クロージャ (closure)


function_object()
