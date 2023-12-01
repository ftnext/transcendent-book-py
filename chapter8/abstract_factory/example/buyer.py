from abc import ABC
from typing import Protocol


class Pet(ABC):
    ...


class PetShopInterface(Protocol):
    def create_pet(self, type: str) -> Pet:
        ...


def buy(pet: Pet):
    print("Buy", pet)


class PetBuyer:
    def buy_pet(self, pet_shop: PetShopInterface, type: str) -> None:
        pet = pet_shop.create_pet(type)
        buy(pet)


if __name__ == "__main__":
    from shop import CatAndDogOnlyPetShop

    shop = CatAndDogOnlyPetShop()
    buyer = PetBuyer()
    buyer.buy_pet(shop, "cat")
