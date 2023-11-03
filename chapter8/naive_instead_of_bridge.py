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


class PrizeItem(PrizeItemInterface):
    def get_material(self) -> Material:
        return self.material

    def get_shape(self) -> Shape:
        return self.shape


class GoldMedalPrizeItem(PrizeItem):
    material = Material.GOLD
    shape = Shape.MEDAL


class SilverCupPrizeItem(PrizeItem):
    material = Material.SILVER
    shape = Shape.CUP


if __name__ == "__main__":
    gold_medal = GoldMedalPrizeItem()
    print(f"{gold_medal.get_material()=}", f"{gold_medal.get_shape()=}")
    print()
    silver_cup = SilverCupPrizeItem()
    print(f"{silver_cup.get_material()=}", f"{silver_cup.get_shape()=}")
