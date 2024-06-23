import pretty_printing

shop_items = {
    "tst": 1,
    "words killed by abilities yield xp": 100,
    "words killed by abilities yield coins": 50,
    "increase freeze duration (+0.4sec)": 25,
    "increase angle view for mega crossbow (+1deg)": 40
}


def shop_for_user(user_id, coins, owned_stuff):

    print(pretty_printing.pretty_print("Shop Menu"))
    while True:
        print("Available items:")

        counter=1
        for item, cost in shop_items.items():
            print(f"({counter}) {item[0].capitalize()}{item[1:]} - {cost} coins")
            #might have bug if not text
            counter+=1

        choice = input("Enter item name to purchase or 'q' to quit: ").strip().lower()
        if not choice or choice == 'q': break #navigate via numbers
        elif choice in shop_items:
            item_cost = shop_items[choice]
            if coins >= item_cost:
                coins -= item_cost

                if choice == "tst":
                    if choice in owned_stuff: owned_stuff[choice] +=1
                    else: owned_stuff[choice] = 1

                print(f"Purchase successful! You now have {coins} coins left.")
            else:
                print("Not enough coins.")
        else:
            print("Invalid item name. Please enter a valid item name.")

    return coins, owned_stuff

