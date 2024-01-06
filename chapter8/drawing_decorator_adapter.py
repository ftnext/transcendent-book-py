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


class DecorativeDrawing:
    def __init__(self, target: DrawingInterface) -> None:
        self.target = target

    def start_at(self, p: Point) -> None:
        self.target.start_at(p)

    def line_to(self, p: Point) -> None:
        self.target.line_to(p)

    def rectangle(self, top_left: Point, bottom_right: Point) -> None:
        top_right = Point(bottom_right.x, top_left.y)
        bottom_left = Point(top_left.x, bottom_right.y)
        self.start_at(top_left)
        self.line_to(top_right)
        self.line_to(bottom_right)
        self.line_to(bottom_left)
        self.line_to(top_left)

    def triangle(self, p0: Point, p1: Point, p2: Point) -> None:
        self.start_at(p0)
        self.line_to(p1)
        self.line_to(p2)
        self.line_to(p0)


class ExampleVendorGraphics:
    def line(self, x0: int, y0: int, x1: int, y1: int) -> None:
        print(f"({x0}, {y0}) から ({x1}, {y1}) まで線を引く")


if __name__ == "__main__":
    drawing = DecorativeDrawing(
        VendorGraphicsDrawingAdapter(ExampleVendorGraphics())
    )
    drawing.rectangle(Point(10, 60), Point(80, 20))
    print()
    drawing.triangle(Point(0, 4), Point(0, 0), Point(3, 0))
