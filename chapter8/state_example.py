from __future__ import annotations

from enum import Enum


class SpeedMeterState(Enum):
    Safe = "safe"
    Danger = "danger"

    def next_state(self, speed: float) -> SpeedMeterState:
        match self:
            case SpeedMeterState.Safe:
                return SpeedMeterState.Danger if speed > 100.0 else self
            case SpeedMeterState.Danger:
                return SpeedMeterState.Safe if speed <= 80.0 else self

    def get_color(self):
        match self:
            case SpeedMeterState.Safe:
                return "green"
            case SpeedMeterState.Danger:
                return "red"


class SpeedMeter:
    def __init__(self) -> None:
        self.speed = 0.0
        self.current_state = SpeedMeterState.Safe

    def set_speed(self, speed: float) -> None:
        self.speed = speed
        self.current_state = self.current_state.next_state(self.speed)

    def display(self) -> str:
        color = self.current_state.get_color()
        return f"{self.speed:.2f}km/h {color}"


if __name__ == "__main__":
    speed_meter = SpeedMeter()
    print(speed_meter.display())

    speed_meter.set_speed(90.0)
    print(speed_meter.display())

    speed_meter.set_speed(101.0)
    print(speed_meter.display())

    speed_meter.set_speed(90.0)
    print(speed_meter.display())

    speed_meter.set_speed(80.0)
    print(speed_meter.display())
