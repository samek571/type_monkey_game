import pretty_printing

#item : (item_price:int, amount_available:int)
# in this case i had no elegant idea how else to represent bools so i came up with this notation
# TODO tweaker could easily break the game, we need some protection on this file and all other files if possible
shop_items = {
    "tst": (1,500),
    "ability kills yield xp": (100,1),
    "ability kills yield coins": (50,1),
    "freeze duration (+0.4sec)": (25, 5),
    "mega crossbow angle view (+1deg)": (40, 10)
}

#owned_stuff
# item:str : owned_amount:int
def shop_for_user(coins, owned_stuff):
    tmp_internal_mapping = {}

    print(pretty_printing.pretty_print("Shop Menu"))
    while True:
        print("\nAvailable items:")
        counter = 1
        for item, (price, available_amount) in shop_items.items():
            owned_amount = owned_stuff.get(item, 0)
            if owned_amount < available_amount:
                print(f"({counter}) {item.capitalize()} - {price} coins (Available: {available_amount - owned_amount})")
                tmp_internal_mapping[str(counter)] = item
                counter += 1

        if counter == 1:
            print("No items available for purchase.")
            print("YOU ALREADY OWN EVERYTHING!")
            break

        choice = input("Enter item name number to purchase or 'q' to quit: ").strip()
        if not choice or choice == 'q': break
        elif choice.isdigit() and choice in tmp_internal_mapping:
            item = tmp_internal_mapping[choice]
            item_price, item_available = shop_items[item]
            if coins >= item_price:
                coins -= item_price
                owned_stuff[item] = owned_stuff.get(item, 0) + 1

                print(f"Purchase successful! You now have {coins} coins left.")
                print(owned_stuff)
            else:
                print("Not enough coins.")
        else:
            print("Invalid item name. Please enter a valid item name.")

    return coins, owned_stuff

#print(shop_for_user(152, {}))