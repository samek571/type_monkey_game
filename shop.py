import pretty_printing

#in this case i had no elegant idea how else to represent bools so i came up with this notation
#item : (item_price:tuple[int], amount_available:int) where len(item_price:tuple) = amount_available
# TODO tweaker could easily break the game, we need some protection on this file and all other files if possible
shop_items = {
    "tst": ((1,2,), 500),
    "ability kills yield xp": ((1000,), 1),
    "ability kills yield coins": ((500,), 1),
    "freeze duration (+0.4sec)": ((25, 50, 75, 100, 125), 5),
    "mega crossbow angle view (+1deg)": ((40, 70, 100, 135, 180, 370, 400, 500, 550, 610), 10),
    "improve randomized value of kick back factor": ((50, 120, 720, 1000), 4)
}

#owned_stuff
# item:str : owned_amount:int
def shop_for_user(coins, owned_stuff):
    tmp_internal_mapping = {}

    print(pretty_printing.pretty_print("Shop Menu"))
    while True:
        print("\nAvailable items:")
        counter = 1
        for item, (prices, available_amount) in shop_items.items():
            owned_amount = owned_stuff.get(item, 0)
            if owned_amount < available_amount:
                if owned_amount < len(prices):next_price = prices[owned_amount]
                else: next_price = prices[-1]

                print(f"({counter}) {item.capitalize()} - {next_price} coins (Available: {available_amount - owned_amount})")
                tmp_internal_mapping[str(counter)] = item
                counter += 1

        if counter == 1:
            print("No items available for purchase.")
            print("YOU ALREADY OWN EVERYTHING!")
            break

        print(f"\nYou have {coins} coins")
        choice = input("Enter item number to purchase or 'q' to quit: ").strip()
        if not choice or choice.lower() == 'q':
            break
        elif choice.isdigit() and choice in tmp_internal_mapping:
            item = tmp_internal_mapping[choice]
            prices, available_amount = shop_items[item]
            owned_amount = owned_stuff.get(item, 0)
            if owned_amount < available_amount:
                if owned_amount < len(prices): item_price = prices[owned_amount]
                else: item_price = prices[-1]
                if coins >= item_price:
                    coins -= item_price
                    owned_stuff[item] = owned_amount + 1

                    pretty_printing.clear_console()
                    print(pretty_printing.pretty_print("Shop Menu"))
                    print(f"Purchase successful! You now have {coins} coins left.")
                    print(owned_stuff)
                else:
                    print("Not enough coins.")
            else:
                print("You already own the maximum amount of this item.")
        else:
            print("Invalid item number. Please enter a valid item number.")

    return coins, owned_stuff

#print(shop_for_user(1521, {}))