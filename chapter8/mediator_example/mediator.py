from subA import MediatorInterfaceA, ObjectA
from subB import MediatorInterfaceB, ObjectB


class Mediator(MediatorInterfaceA, MediatorInterfaceB):
    def __init__(self):
        self.a = ObjectA(self)
        self.b = ObjectB(self)

    def notify_activity_done(self):
        print("notify_activity_done from MediatorInterfaceA")
        self.b.do_task()

    def notify_task_completion(self):
        print("notify_task_completion from MediatorInterfaceB")
        self.a.finish_the_work()


if __name__ == "__main__":
    mediator = Mediator()
    mediator.notify_activity_done()
    print()
    mediator.a.some_activity()
