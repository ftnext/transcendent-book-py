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
    def get_material(self) -> Material:
        raise NotImplementedError


class PrizeShape(ABC):
    @abstractmethod
    def get_shape(self) -> Shape:
        raise NotImplementedError


class PrizeMaterialGold(PrizeMaterial):
    def get_material(self) -> Material:
        return Material.GOLD


class PrizeMaterialSilver(PrizeMaterial):
    def get_material(self) -> Material:
        return Material.SILVER


class PrizeMaterialBronze(PrizeMaterial):
    def get_material(self) -> Material:
        return Material.BRONZE


class PrizeShapeMedal(PrizeShape):
    def get_shape(self) -> Shape:
        return Shape.MEDAL


class PrizeShapeCup(PrizeShape):
    def get_shape(self) -> Shape:
        return Shape.CUP


# PrizeItemクラスを設けずに具体的な賞品を表すクラスを多重継承で実現できる


class GoldMedalPrizeItem(
    PrizeMaterialGold, PrizeShapeMedal, PrizeItemInterface
):
    ...


class SilverCupPrizeItem(
    PrizeMaterialSilver, PrizeShapeCup, PrizeItemInterface
):
    ...


if __name__ == "__main__":
    gold_medal = GoldMedalPrizeItem()
    print(f"{gold_medal.get_material()=}", f"{gold_medal.get_shape()=}")
    print()
    silver_cup = SilverCupPrizeItem()
    print(f"{silver_cup.get_material()=}", f"{silver_cup.get_shape()=}")
