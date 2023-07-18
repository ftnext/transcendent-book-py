class Body:
    ...


class Engine:
    def start(self) -> None:
        ...


class Wheel:
    def adjust(self) -> None:
        ...


class Car:
    def __init__(
        self, body: Body, engine: Engine, wheels: list[Wheel]
    ) -> None:
        self.body = body
        self.engine = engine
        self.wheels = wheels

    def start_engine(self) -> None:
        self.engine.start()

    def adjust_handle(self) -> None:
        self.wheels[0].adjust()


if __name__ == "__main__":
    wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
    car = Car(Body(), Engine(), wheels)

    car.start_engine()
    car.adjust_handle()
