from shop import Pet, PetShop


def buy(pet: Pet):
    print("Buy", pet)


class PetBuyer:
    def buy_pet(self, pet_shop: PetShop, type: str) -> None:
        pet = pet_shop.create_pet(type)
        buy(pet)


if __name__ == "__main__":
    shop = PetShop()
    buyer = PetBuyer()
    buyer.buy_pet(shop, "cat")
