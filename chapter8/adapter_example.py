from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Point:
    x: int
    y: int


class DrawingInterface(Protocol):
    def start_at(self, p: Point) -> None:
        ...

    def line_to(self, p: Point) -> None:
        ...


class VendorGraphicsInterface(Protocol):
    def line(self, x0: int, y0: int, x1: int, y1: int) -> None:
        ...


class VendorGraphicsDrawingAdapter:
    def __init__(self, target: VendorGraphicsInterface) -> None:
        self.target = target
        self.current: Point | None = None

    def start_at(self, p: Point) -> None:
        self.current = p

    def line_to(self, p: Point) -> None:
        if self.current is None:
            raise RuntimeError()

        p0 = self.current
        self.target.line(p0.x, p0.y, p.x, p.y)
        self.current = p


class ExampleVendorGraphics:
    def line(self, x0: int, y0: int, x1: int, y1: int) -> None:
        print(f"({x0}, {y0}) から ({x1}, {y1}) まで線を引く")


if __name__ == "__main__":
    drawing = VendorGraphicsDrawingAdapter(ExampleVendorGraphics())
    drawing.start_at(Point(5, 40))
    drawing.line_to(Point(20, 10))
