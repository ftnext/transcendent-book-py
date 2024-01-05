from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class DrawingInterface(Protocol):
    def start_at(self, p: Point) -> None:
        ...

    def line_to(self, p: Point) -> None:
        ...


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
        # 左上 -> 右上 -> 右下 -> 左下 -> 左上 と線を引く
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


class ExampleDrawing:
    def start_at(self, p: Point) -> None:
        print(f"始点 {p}")

    def line_to(self, p: Point) -> None:
        print(f"{p} まで線を引いて移動")


if __name__ == "__main__":
    drawing = DecorativeDrawing(ExampleDrawing())
    drawing.rectangle(Point(10, 60), Point(80, 20))
    print()
    drawing.triangle(Point(0, 4), Point(0, 0), Point(3, 0))
