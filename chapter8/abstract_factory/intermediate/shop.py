from abc import ABC


class Pet(ABC):
    ...


class Cat(Pet):
    ...


class Dog(Pet):
    ...


class PetShop:
    def create_pet(self, type: str) -> Pet:
        match type:
            case "cat":
                return Cat()
            case "dog":
                return Dog()
            case _:
                raise ValueError(type)
