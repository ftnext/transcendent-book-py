from typing import Protocol


class MediatorInterfaceA(Protocol):
    def notify_activity_done(self):
        ...


class ObjectA:
    def __init__(self, mediator: MediatorInterfaceA) -> None:
        self.mediator = mediator

    def some_activity(self):
        print(self.__class__.__name__, "some_activity")
        self.mediator.notify_activity_done()

    def finish_the_work(self):
        print(self.__class__.__name__, "finish_the_work")
