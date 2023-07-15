from typing import Protocol


class Pet(Protocol):
    def react(self) -> None:
        ...


class PetShopCustomer:
    def touch(self, pet: Pet) -> None:
        pet.react()


class Dog:
    def react(self) -> None:
        print("ワン")


class Cat:
    def react(self) -> None:
        print("ニャン")


if __name__ == "__main__":
    customer = PetShopCustomer()
    customer.touch(Dog())
    customer.touch(Cat())

"""
% python polymorphism_pet.py
ワン
ニャン
"""
