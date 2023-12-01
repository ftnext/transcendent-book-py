from buyer import Pet, PetShopInterface


class Cat(Pet):
    ...


class Dog(Pet):
    ...


class CatAndDogOnlyPetShop(PetShopInterface):
    def create_pet(self, type: str) -> Pet:
        match type:
            case "cat":
                return Cat()
            case "dog":
                return Dog()
            case _:
                raise ValueError(type)
