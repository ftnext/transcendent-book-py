from ui import SelectionUI
from use_case import BuyPetCommand, CancelBuyingCommand, Cat, Dog, PetShop


def create_pet_selection_ui(shop: PetShop):
    ui = SelectionUI()
    ui.register_command("猫をください", BuyPetCommand(shop, Cat()))
    ui.register_command("犬をください", BuyPetCommand(shop, Dog()))
    ui.register_command("やっぱりやめます", CancelBuyingCommand(shop))
    return ui


if __name__ == "__main__":
    shop = PetShop()
    ui = create_pet_selection_ui(shop)
    print(ui.help())
    print()

    user_input = int(input("数字を入力: "))
    ui.select(user_input)
