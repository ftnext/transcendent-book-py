from typing import Protocol


class FacadeInterface(Protocol):
    def simple_action(self):
        ...


def use_facade(facade: FacadeInterface):
    facade.simple_action()


class FeatureA:
    def complex_processA(self):
        print("process A")


class FeatureB:
    def complex_processB(self):
        print("process B")


class FeatureC:
    def complex_processC(self):
        print("process C")


class Facade:
    a = FeatureA()
    b = FeatureB()
    c = FeatureC()

    def simple_action(self):
        self.a.complex_processA()
        self.b.complex_processB()
        self.c.complex_processC()


if __name__ == "__main__":
    use_facade(Facade())
