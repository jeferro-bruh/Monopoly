"""
landing_logic.py

Spence

A copy of property_action.py to incorporate board_data variables. I Jethro modified some
of the existing code provided by Spence to use my variables. I deleted some lines as well
while attempting to fix some of the errors that caused problems.
"""

from typing import Any
from board_data import jail_position, board_data
from playing_cards import draw_card, chance_cards, chest_cards, activate_card


def offer_purchase(player: int, space: dict[str, Any], money:list[int]) -> None: # Function for buying properties and obtaining ownership

    print(f"You landed on {space['name']}!")
    print(f"Purchase price: ${space['price']}")
    
    choice = input("Would you like to buy this property? (Yes/No): ")
    
    if choice.title() == "Yes": # If player chooses to buy the property
    
        if money[player] >= space["price"]: # If player has enough money to purchase the property
    
            money[player] -= space["price"]
            space["owner"] = player
    
            print(f"You purchased {space['name']}!")
            print(f"Balance: ${money[player]}")
                
        else: # If player cannot afford the property
            print("You do not have sufficient funds!")

            raise_money(player, space["price"], money) # Give player opportunity to raise funds

            if money[player] >= space["price"]: # If player has raised enough funds to purchase the property
                choice = input("You now have sufficient funds! Buy property? (Yes/No): ")
            
                if choice.title() == "Yes": # If player chooses to buy the property after raising funds

                    money[player] -= space["price"]
                    space["owner"] = player

                    print(f"You purchased {space['name']}!")
                    print(f"Balance: ${money[player]}")
def mortgage_prop(player: int) -> None:
    print("Work in progress") # still working on this #FIX
def sell_house(player: int) -> None:
    print("Work in progress") # still working on this #FIX

def raise_money(player: int, amount_needed: int, money: list[int]) -> None: # Function for raising funds when a player cannot afford a payment
    while money[player] < amount_needed: # Allow player to raise funds until they can afford the payment or chooses to stop

        print("\nHow would you like to raise funds?")
        print("1. Mortgage Properties")
        print("2. Sell Houses and Hotels")
        print("3. Done")

        choice = input("> ")

        if choice == "1": # Raise money through mortgaging properties
            mortgage_prop(player)

        elif choice == "2": # Raise money through selling houses or hotels
            sell_house(player)

        elif choice == "3": # Player is done attempting to raise money
            break

        else:
            print("Invalid choice.")


def bankrupt(player: int, money: list[int], creditor: int | None) -> None: # Function for handling bankruptcies and transferring eliminated player's properties

    print(f"{player + 1} is bankrupt!")

    if creditor is not None:

        # Transfer all remaining money from bankrupt player
        if money[player] > 0:
            money[creditor] += money[player]

    # Remove all assets from bankrupt player
    money[player] = 0

def count_railroads(owner: int, board_data: list[dict[str, Any]]) -> int: # Returns the number of railroads owned by a specified owner
    count = 0

    for space in board_data:
        if space["type"] == "railroad" and space["owner"] == owner:
            count += 1

    return count

def count_utilities(owner: int, board_data: list[dict[str, Any]]) -> int: # Returns the number of utilities owned by a specified owner
    count = 0

    for space in board_data:
        if space["type"] == "utility" and space["owner"] == owner:
            count += 1

    return count

def landing_thing(player: int, positions: list[int], money: list[int], dice_total: int) -> None:

    standing = positions[player] # gets player pos
    space: dict[str, Any] = board_data[standing] # space = where they are 'standing'

    if space["type"] == "property": # Checks whether the space is a colored property

        if space["owner"] is None: # Checks if the property is unowned
            offer_purchase(player, space, money) # Offer player the opportunity to buy the property

        elif space["owner"] == player: # Checks if the current player owns this property

            print(f"You already own {space['name']}. "
                "Go inside and take a load off!"
            )

        else:
            rent_due = space["rent"][space["houses"]] # Calculates rent based on property development

            print(
                f"You owe ${rent_due} in rent to "
                f"{space['owner']}!"
            )

            if money[player] < rent_due: # Checks whether the player can afford the rent

                print("You do not have enough money!")

                # Allow player to sell assets to raise money
                raise_money(player, rent_due, money)

                if money[player] < rent_due:

                    bankrupt(player, money, space["owner"])
                    return

            # Transfers rent from player to property owner
            money[player] -= rent_due
            money[space["owner"]] += rent_due
            print(f"Balance: ${money[player]}")

    elif space["type"] == "railroad": # Checks whether the space is a railroad

        if space["owner"] is None: # Checks if the railroad is unowned
            offer_purchase(player, space, money) # Offer player the opportunity to buy the railroad

        elif space["owner"] == player: # Checks if the current player owns this railroad

            print(f"You already own {space['name']}. "
                "Relax and take a ride around the block!"
            )

        else:
            railroads_owned = count_railroads(space["owner"], board_data) # Calculates rent based on number of railroads owned

            if railroads_owned == 1:
                rent_due = 25
            elif railroads_owned == 2:
                rent_due = 50
            elif railroads_owned == 3:
                rent_due = 100
            else:
                rent_due = 200 # If a player owns all 4 railroads this will activate

            print(
                f"You owe ${rent_due} to "
                f"{space['owner']}!"
            )

            if money[player] < rent_due: # Checks whether the player can afford the rent

                print("You do not have enough funds!")

                # Allow player to sell assets to raise money
                raise_money(player, rent_due, money)

                if money[player] < rent_due:

                    bankrupt(player, money, space["owner"])
                    return

            # Transfers rent from player to railroad owner
            money[player] -= rent_due
            money[space["owner"]] += rent_due
            print(f"Balance: ${money[player]}")

    elif space["type"] == "utility": # Checks whether the space is a utility

        if space["owner"] is None: # Checks if the utility is unowned
            offer_purchase(player, space, money) # Offer player the opportunity to buy the utility

        elif space["owner"] == player: # Checks if the current player owns this utility

            print(f"You already own {space['name']}. ")

        else:
            utilities_owned = count_utilities(space["owner"], board_data) # Calculates rent based on number of utilities owned

            if utilities_owned == 1:
                rent_due = dice_total * 4
            else:
                rent_due = dice_total * 10 # If a player owns both utilities this will activate

            print(
                f"You owe ${rent_due} to "
                f"{space['owner']}!"
            )

            if money[player] < rent_due: # Checks whether the player can afford the rent

                print("You do not have enough funds!")

                # Allow player to sell assets to raise money
                raise_money(player, rent_due, money)

                if money[player] < rent_due:
                    bankrupt(player, money, space["owner"])
                    return

            # Transfers rent from player to utility owner
            money[player] -= rent_due
            money[space["owner"]] += rent_due
            print(f"Balance: ${money[player]}")

    elif space["type"] == "chance": # Checks if the player landed on a Chance space
        card = draw_card(chance_cards)
        print(card['text'])
        activate_card(card, player, positions, money)

    elif space["type"] == "chest": # Checks if the player landed on a Community Chest space
        card = draw_card(chest_cards)
        print(card['text'])
        activate_card(card, player, positions, money)

    elif space["type"] == "income_tax": # Checks if the player landed on Income Tax

        tax = money[player] // 10 # Calculate tax as 10% of available cash

        money[player] -= tax

        print(f"You paid ${tax} in income tax!")
        print(f"Balance: ${money[player]}")

    elif space["type"] == "visiting_jail": # Checks if the player landed on "Just Visiting"

        print("Relax, you're just visiting jail.")

    elif space["type"] == "go_to_jail": # Checks if the player landed on "Go To Jail"

        print("Call your lawyer, you're going directly to jail!")
        positions[player] = jail_position # 41 is jail's board_data position

    elif space["type"] == "luxury_tax": # Checks if the player landed on "Luxury Tax"

        tax_due = space["amount"] # Luxury Tax fee

        if money[player] < tax_due: # Checks whether the player can afford the fee

            print("You do not have enough funds!")

            # Allow player to sell assets to raise money
            raise_money(player, tax_due, money)

            if money[player] < tax_due:
                bankrupt(player, money, None)
                return

        money[player] -= tax_due
        print(f"You paid ${tax_due} for luxury tax!")
        print(f"Balance: ${money[player]}")

    elif space["type"] == "go": # Checks if the player landed on "Go"

        print("You landed on GO; WHOOP, WHOOP! Collect $200!")
        print(f"Balance: ${money[player]}")

    else: # Free Parking is the only remaining board_data space
        print("Congratulations you found free parking!")
        print("Not an easy feat around here!")

if __name__ == '__main__':
    positions = [39, 0]
    money = [100, 100]
    landing_thing(0, positions, money, 7)
    print(money)
