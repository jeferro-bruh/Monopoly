"""
board_data.py
Jethro AA
Created on  Oct. 17th 2026

Here I am creating the main data for our board and its respective spots.
I am using a list of dictionaries with the hope of making calling differnet spots easy.
"""
# Importing Any to use in my dictionary that will contain many different types.
from typing import Any

# I wanted to make the house info a function to easily return my values making my code less.. thick?
def house_func(name: str, color: str, price: int, rent: int) -> dict[str, Any]:
    """
    Here I have a function for my house dict to try and make it more organized.

    Parameters
    ----------
    name : str
        name of the spot like brown property, etc
    color : str
        color of property like brown
    price : int
        the price of the house (refer to spence?)
    rent : int
        price of renting (refer to spence?)

    Returns
    -------
    location
        the main properties of the location are outputted.
    """
    return {'name': name,
            'type': 'house',
            'color': color,
            'price': price,
            'rent': rent}

# the position of start and jail

starting_position = 0
jail_position = 9


# Here board_data is a list of dictionaries
# I have the board 'name' along with the spots name that will be printed.
# the 'type' key is for what this spot is
# 'price' key is a place holder for now since Spence is doing the money sys  will ask later...
# house_func() is my function to make adding house data easier later.
# I might make the others functions later but as of now I don't see any reason to.

board_data: list[dict[str, Any]] = [
    {'name': 'Go', 'type': 'go', 'salary': 0}, # starting position
    house_func('Mediterranean Ave', 'brown', 0, 0), # brown 1 (cheapest ones)
    {'name': 'Community Chest #1', 'type': 'chest'},
    house_func('Baltic Ave', 'brown', 0, 0), # brown 2 (cheapest ones)
    {'name': 'Income Tax', 'type': 'tax', 'amount': 0}, # This first spot is "10%" of income
    house_func('Oriental Ave', 'grey', 0, 0), # grey 1
    house_func('Vermont Ave', 'grey', 0, 0), # grey 2
    {'name': 'Chance #1', 'type': 'chance'},
    house_func('Connecticut Ave', 'grey', 0, 0), # grey 3
    {'name': 'Just Visiting / Jail', 'type': 'visiting_jail'},
    house_func('St. Charles Place', 'pink', 0, 0), # pink 1
    house_func('States Ave', 'pink', 0, 0), # pink 2
    house_func('Virginia Ave', 'pink', 0, 0), # pink 3
    house_func('St. James Place', 'orange', 0, 0), # orange 1
    {'name': 'Community Chest #2', 'type': 'chest'},
    house_func('Tennessee Ave', 'orange', 0, 0), # orange 2
    house_func('New York Ave', 'orange', 0, 0), # orange 3
    {'name': 'Free Parking', 'type': 'free_spot'},
    house_func('Kentucky Ave', 'red', 0, 0), # red 1
    {'name': 'Chance #2', 'type': 'chance'},
    house_func('Indiana Ave', 'red', 0, 0), # red 2
    house_func('Illinois Ave', 'red', 0, 0), # red 3
    house_func('Atlantic Ave', 'yellow', 0, 0), # yellow  1
    house_func('Ventnor Ave', 'yellow', 0, 0), # yellow  2
    house_func('Marvin Gardens', 'yellow', 0, 0), # yellow  3
    {'name': 'Go To Jail!', 'type': 'go_to_jail'},
    house_func('Pacific Ave', 'green', 0, 0), # green  1
    house_func('North Carolina Ave', 'green', 0, 0), # green  2
    {'name': 'Community Chest #3', 'type': 'chest'},
    house_func('Pennsylvania Ave', 'green', 0, 0), # green  3
    {'name': 'Chance #3', 'type': 'chance'},
    house_func('Park Place', 'blue', 0, 0), # blue 1 (most expensive ones)
    {'name': 'Luxury Tax', 'type': 'tax', 'amount': 0}, # flat rate tax
    house_func('Boardwalk', 'blue', 0, 0), # blue 2 (most expensive ones)
]
