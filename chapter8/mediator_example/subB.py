from typing import Protocol


class MediatorInterfaceB(Protocol):
    def notify_task_completion(self):
        ...


class ObjectB:
    def __init__(self, mediator: MediatorInterfaceB) -> None:
        self.mediator = mediator

    def do_task(self):
        print(self.__class__.__name__, "do_task")
        self.mediator.notify_task_completion()
