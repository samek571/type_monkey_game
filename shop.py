import pretty_printing

#key: (actual value, price, len)
shop_items = {
    "tst": ((1,), (1,2,), 500),
    "ability kills yield xp": ((True), (1,), 1),
    "ability kills yield coins": ((True), (500,), 1),
    "killing n closest enemies (+1)": ((4,5,6,7),(40, 100, 140, 400),4),
    "freeze duration (+0.4sec)": ((4000, 4400, 4800, 5200, 5600, 6000), (25, 50, 75, 100, 125, 200), 6),
    "mega crossbow angle view (+1deg)": ((16, 17, 18, 19, 20, 21, 22, 23, 24, 25), (40, 70, 100, 135, 180, 370, 400, 500, 550, 610), 10),
    "improve randomized value of kick back factor": ((12, 14, 17, 20), (50, 100, 150, 600), 4),
    "kick back severity (+1word)": ((4,5,6,7), (60, 120, 250, 500), 4),
}

def shop_for_user(coins, owned_stuff):
    tmp_internal_mapping = {}

    print(pretty_printing.pretty_print("Shop Menu"))
    while True:
        print("\nAvailable items:")
        counter = 1
        for item, (values, prices, available_amount) in shop_items.items():
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
            values, prices, available_amount = shop_items[item]
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


#print(shop_for_user(12521, {}))