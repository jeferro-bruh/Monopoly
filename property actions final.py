import random

players = [
    {
        "name": "Player 1",
        "money": 1500,
        "position": 0,
        "properties": []
    },
    {
        "name": "Player 2",
        "money": 1500,
        "position": 0,
        "properties": []
    }
]

def offer_purchase(player, space): # Function for buying properties and obtaining ownership

    print(f"You landed on {space['name']}!")
    print(f"Purchase price: ${space['price']}")
    
    choice = input("Would you like to buy this property? (Yes/No): ")
    
    if choice.title() == "Yes": # If player chooses to buy the property
    
        if player["money"] >= space["price"]: # If player has enough money to purchase the property
    
            player["money"] -= space["price"]
            space["owner"] = player["name"]
            player["properties"].append(space)
    
            print(f"You purchased {space['name']}!")
            print(f"Balance: ${player['money']}")
                
        else: # If player cannot afford the property
            print("You do not have sufficient funds!")

            raise_money(player, space["price"]) # Give player opportunity to raise funds

            if player["money"] >= space["price"]: # If player has raised enough funds to purchase the property
                choice = input("You now have sufficient funds! Buy property? (Yes/No): ")
            
                if choice.title() == "Yes": # If player chooses to buy the property after raising funds

                    player["money"] -= space["price"]
                    space["owner"] = player["name"]
                    player["properties"].append(space)

                    print(f"You purchased {space['name']}!")
                    print(f"Balance: ${player['money']}")

def raise_money(player, amount_needed): # Function for raising funds when a player cannot afford a payment
    while player["money"] < amount_needed: # Allow player to raise funds until they can afford the payment or chooses to stop

        print("\nHow would you like to raise funds?")
        print("1. Mortgage Properties")
        print("2. Sell Houses and Hotels")
        print("3. Done")

        choice = input("> ")

        if choice == "1": # Raise money through mortgaging properties
            mortgage_property(player)

        elif choice == "2": # Raise money through selling houses or hotels
            sell_house(player)

        elif choice == "3": # Player is done attempting to raise money
            break

        else:
            print("Invalid choice.")

def pay_player(payer, receiver, amount): # Function for handling payments between players

    if payer["money"] < amount:

        print(f"{payer['name']} cannot afford ${amount}!")

        raise_money(payer, amount)

        if payer["money"] < amount:
            print(f"{payer['name']} is bankrupt!")
            return False

    payer["money"] -= amount
    receiver["money"] += amount

    print(
        f"{payer['name']} paid ${amount} to "
        f"{receiver['name']}. "
        f"Remaining balance: ${payer['money']}"
    )

    return True

def bankrupt(player, creditor=None): # Function for handling bankruptcies and transferring eliminated player's properties

    print(f"{player['name']} is bankrupt!")

    if creditor is not None:

        # Transfer ownership of each property
        for property in player["properties"]:
            property["owner"] = creditor["name"]

        # Add properties to the creditor's property list
        creditor["properties"].extend(player["properties"])

        # Transfer all remaining money from bankrupt player
        if player["money"] > 0:
            creditor["money"] += player["money"]

    # Remove all assets from bankrupt player
    player["properties"].clear()
    player["money"] = 0

def find_owner(owner_name): # Function that returns the player dictionary matching the owner's name
    for player in players:
        if player["name"] == owner_name:
            return player
    return None

def draw_card(player, deck): # Draws and applies a Chance or Community Chest card

    card = random.choice(deck) # Select a random card from the deck

    print(card["text"])

    # Apply money gain or loss
    if "money" in card:

        amount = card["money"]

        if amount < 0: # Player is charged

            amount_due = abs(amount)

            if player["money"] < amount_due:
                print("You do not have enough funds!")

                raise_money(player, amount_due)

                if player["money"] < amount_due:

                    bankrupt(player, None)
                    return

            player["money"] -= amount_due

        else: # Player receives money

            player["money"] += amount

        print(f"Balance: ${player['money']}")

    # Move player if the card changes the player's position
    if "position" in card:
        player["position"] = card["position"]

def count_railroads(owner, board): # Returns the number of railroads owned by a specified owner
    count = 0

    for space in board:
        if space["type"] == "railroad" and space["owner"] == owner:
            count += 1

    return count

def count_utilities(owner, board): # Returns the number of utilities owned by a specified owner
    count = 0

    for space in board:
        if space["type"] == "utility" and space["owner"] == owner:
            count += 1

    return count

######

if space["type"] == "property": # Checks whether the space is a colored property

    if space["owner"] is None: # Checks if the property is unowned
        offer_purchase(player, space) # Offer player the opportunity to buy the property

    elif space["owner"] == player["name"]: # Checks if the current player owns this property

        print(f"You already own {space['name']}. "
              "Go inside and take a load off!"
        )

    else:
        owner = find_owner(space["owner"]) # Finds the space's owner

        rent_due = space["rent"][space["houses"]] # Calculates rent based on property development

        print(
            f"You owe ${rent_due} in rent to "
            f"{space['owner']}!"
        )

        if player["money"] < rent_due: # Checks whether the player can afford the rent

            print("You do not have enough money!")

            # Allow player to sell assets to raise money
            raise_money(player, rent_due)

            if player["money"] < rent_due:

                bankrupt(player, owner)
                return

        # Transfers rent from player to property owner
        player["money"] -= rent_due
        owner["money"] += rent_due
        print(f"Balance: ${player['money']}")

elif space["type"] == "railroad": # Checks whether the space is a railroad

    if space["owner"] is None: # Checks if the railroad is unowned
        offer_purchase(player, space) # Offer player the opportunity to buy the railroad

    elif space["owner"] == player["name"]: # Checks if the current player owns this railroad

        print(f"You already own {space['name']}. "
              "Relax and take a ride around the block!"
        )

    else:
        owner = find_owner(space["owner"]) # Finds the space's owner

        railroads_owned = count_railroads(space["owner"], board) # Calculates rent based on number of railroads owned

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

        if player["money"] < rent_due: # Checks whether the player can afford the rent

            print("You do not have enough funds!")

            # Allow player to sell assets to raise money
            raise_money(player, rent_due)

            if player["money"] < rent_due:

                bankrupt(player, owner)
                return

        # Transfers rent from player to railroad owner
        player["money"] -= rent_due
        owner["money"] += rent_due
        print(f"Balance: ${player['money']}")

elif space["type"] == "utility": # Checks whether the space is a utility

    if space["owner"] is None: # Checks if the utility is unowned
        offer_purchase(player, space) # Offer player the opportunity to buy the utility

    elif space["owner"] == player["name"]: # Checks if the current player owns this utility
        
        print(f"You already own {space['name']}. ")
    
    else:
        owner = find_owner(space["owner"]) # Finds the space's owner

        utilities_owned = count_utilities(space["owner"], board) # Calculates rent based on number of utilities owned

        if utilities_owned == 1:
            rent_due = dice_total * 4
        else:
            rent_due = dice_total * 10 # If a player owns both utilities this will activate

        print(
            f"You owe ${rent_due} to "
            f"{space['owner']}!"
        )

        if player["money"] < rent_due: # Checks whether the player can afford the rent
        
            print("You do not have enough funds!")

            # Allow player to sell assets to raise money
            raise_money(player, rent_due)
            
            if player["money"] < rent_due:
            
                bankrupt(player, owner)
                return

        # Transfers rent from player to utility owner
        player["money"] -= rent_due
        owner["money"] += rent_due
        print(f"Balance: ${player['money']}")

elif space["type"] == "chance": # Checks if the player landed on a Chance space
    draw_card(player, chance_cards) # Draw and apply a Chance Card

elif space["type"] == "community_chest": # Checks if the player landed on a Community Chest space
    draw_card(player, community_cards) # Draw and apply a Community Chest card

elif space["type"] == "income_tax": # Checks if the player landed on Income Tax

    tax = player["money"] // 10 # Calculate tax as 10% of available cash

    player["money"] -= tax

    print(f"You paid ${tax} in income tax!")
    print(f"Balance: ${player['money']}")

elif space["type"] == "just_visiting": # Checks if the player landed on "Just Visiting"

    print("Relax, you're just visiting jail.")

elif space["type"] == "go_to_jail": # Checks if the player landed on "Go To Jail"

    print("Call your lawyer, you're going directly to jail!")
    player["position"] = 41 # 41 is jail's board position

elif space["type"] == "luxury_tax": # Checks if the player landed on "Luxury Tax"

    tax_due = 75 # Luxury Tax fee

    if player["money"] < tax_due: # Checks whether the player can afford the fee

        print("You do not have enough funds!")

        # Allow player to sell assets to raise money
        raise_money(player, tax_due)

        if player["money"] < tax_due:

            bankrupt(player, None)
            return

    player["money"] -= tax_due
    print("You paid $75 for luxury tax!")
    print(f"Balance: ${player['money']}")

elif space["type"] == "go": # Checks if the player landed on "Go"

    print("You landed on GO; WHOOP, WHOOP! Collect $200!")
    print(f"Balance: ${player['money']}")

else: # Free Parking is the only remaining board space
    print("Congratulations you found free parking!")
    print("Not an easy feat around here!")
