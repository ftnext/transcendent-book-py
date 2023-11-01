import enum
from abc import ABC, abstractmethod


class Material(enum.Enum):
    GOLD = "金"
    SILVER = "銀"
    BRONZE = "銅"


class Shape(enum.Enum):
    MEDAL = "メダル"
    CUP = "カップ"


class PrizeItemInterface(ABC):
    @abstractmethod
    def get_material(self) -> Material:
        raise NotImplementedError

    @abstractmethod
    def get_shape(self) -> Shape:
        raise NotImplementedError


class PrizeMaterial(ABC):
    @abstractmethod
    def get(self) -> Material:
        raise NotImplementedError


class PrizeShape(ABC):
    @abstractmethod
    def get(self) -> Shape:
        raise NotImplementedError


class PrizeItem(PrizeItemInterface):
    def __init__(self, material: PrizeMaterial, shape: PrizeShape) -> None:
        self.material = material
        self.shape = shape

    def get_material(self) -> Material:
        return self.material.get()

    def get_shape(self) -> Shape:
        return self.shape.get()


class PrizeMaterialGold(PrizeMaterial):
    def get(self) -> Material:
        return Material.GOLD


class PrizeMaterialSilver(PrizeMaterial):
    def get(self) -> Material:
        return Material.SILVER


class PrizeMaterialBronze(PrizeMaterial):
    def get(self) -> Material:
        return Material.BRONZE


class PrizeShapeMedal(PrizeShape):
    def get(self) -> Shape:
        return Shape.MEDAL


class PrizeShapeCup(PrizeShape):
    def get(self) -> Shape:
        return Shape.CUP


if __name__ == "__main__":
    gold_medal = PrizeItem(PrizeMaterialGold(), PrizeShapeMedal())
    print(f"{gold_medal.get_material()=}", f"{gold_medal.get_shape()=}")
    print()
    silver_cup = PrizeItem(PrizeMaterialSilver(), PrizeShapeCup())
    print(f"{silver_cup.get_material()=}", f"{silver_cup.get_shape()=}")

"""
gold_medal.get_material()=<Material.GOLD: '金'> gold_medal.get_shape()=<Shape.MEDAL: 'メダル'>

silver_cup.get_material()=<Material.SILVER: '銀'> silver_cup.get_shape()=<Shape.CUP: 'カップ'>
"""
