from abc import ABCMeta

from common import CommandInterface


class PetShop:
    ...


class Pet(metaclass=ABCMeta):
    ...


class Cat(Pet):
    ...


class Dog(Pet):
    ...


class BuyPetCommand(CommandInterface):
    def __init__(self, shop: PetShop, pet: Pet) -> None:
        self.shop = shop
        self.pet = pet

    def invoke(self) -> None:
        print(f"{self.shop} から {self.pet} を購入")


class CancelBuyingCommand(CommandInterface):
    def __init__(self, shop: PetShop) -> None:
        self.shop = shop

    def invoke(self) -> None:
        print(f"{self.shop} にキャンセル申し出")
