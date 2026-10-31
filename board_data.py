"""
board_data.py
Jethro AA
Created on  Oct. 17th 2026

Here I am creating the main data for our board and its respective spots.
I am using a list of dictionaries with the hope of making calling differnet spots easy.

Update - Oct 23/24th
    I am adding the railroad / utility spots to my code to ensure we hit 40 total spots.

    I am also making more functions to easily add info to each spot later if needed.

    * still need key money systems in game, like morgage calc, renting systems, etc (WIP)

    I also realized that im goofy and forgot that the spots for houses are PROPERTIES
        where you can build multiple houses on so im *CHANGING MY FUNCTION NAME*
        to make it less confusing and adding some data for those upgrades.

    Finally I added a helper function! This function takes your color input and 
    spits back out the position where they lay. Should be useful.

Update - Oct 29th/30th
    I am added some extra variables to fulfil the scope of property_actions when I combine it
    into the copy file 'landing_logic.py'.
"""
# Importing Any to use in my dictionary that will contain many different types.
from typing import Any

def property_func(
        name: str,
        color: str,
        price: int,
        house_cost: int,
        rent: list[int]
        ) -> dict[str, Any]:
    """
    Here I have a function for my property dict to try and make it more organized.
    * keep in mind that rent only goes to 4 houses right now, with no hotel planned yet.

    Parameters
    ----------
    name : str
        name of the spot like brown property, etc
    color : str
        color of property like brown
    price : int
        the price of the property
    house_cost : int
        The cost of a adding another house to the property
    rent : list[int]
        price of renting in a list so it can scale with amount on property.

    Returns
    -------
    location
        a dictionary that describes the property on that spot.
    """
    return {
        'name': name,
        'type': 'property',
        'color': color,
        'price': price,
        'house_cost': house_cost,
        'rent': rent,
        'owner': None,
        'houses': 0
    }

def railroad_func(
        name: str,
        price: int,
        rent: int) -> dict[str, Any]:
    """
    Heres my railroad function with it I can track the names, and prices.

    Parameters
    ----------
    name : str
        name of the spot based on where called
    price : int
        specific price based on spot where called
    rent : int
        the rent for this spot here

    Returns
    -------
    dict[str, Any]
        refers to my main dictionary board_data where I have multiple different types
    """
    return {
        'name': name,
        'type': 'railroad',
        'price': price,
        'rent': rent,
        'owner': None,
    }

def taxspot_func(
        name: str,
        tax: int,
        spot_type: str) -> dict[str, Any]:
    """
    My taxspot function is for the two spots on the board involving taxes.

    Parameters
    ----------
    name : str
        For the specific name of the spot
    tax : int
        The tax to be paid by the lander.
    spot_type: str
        spot type helps keep track of what TYPE of taxing we are calculating.

    Returns
    -------
    dict[str, Any]
        refers to my main dictionary board_data where I have multiple different types
    """
    return {
        'name': name,
        'type': spot_type,
        'amount': tax
    }

def utility_func(
        name: str,
        price: int,
        rent: int) -> dict[str, Any]:
    """
    A function for my utilities on the board.

    Parameters
    ----------
    name : str
        The specific name at that spot
    price : int
        The specific price at that spot.
    rent : int
        The specific rent at that spot

    Returns
    -------
    dict[str, Any]
        refers to my main dictionary board_data where I have multiple different types
    """
    return {
        'name': name,
        'type': 'utility',
        'price': price,
        'rent': rent,
        'owner': None,
    }

def gendata_func(
        name: str,
        spot_type: str) -> dict[str, Any]:
    """
    This function is for simple spots that dont require more than a name and
    a defining notion of the 'spot type'.

    Parameters
    ----------
    name : str
        The specific name at that spot on the board.
    spot_type : str
        what type of spot this is.

    Returns
    -------
    dict[str, Any]
        refers to my main dictionary board_data where I have multiple different types
    """
    return {
        'name': name,
        'type': spot_type
    }

def color_pos_func(color: str) -> list[int]:
    """
    A function that helps you get the positions for specific colors.

    Parameters
    ----------
    color : str
        the inputted colored that will be checked if true.

    Returns
    -------
    list[int]
        You get back a list of the positions on the board where those colors sit.
    """
    # here items is a empty list that fills with numbers that are the desired colors spot
    items: list[int] = []
    for i, spot in enumerate(board_data):
        if spot.get('color') == color:
            items.append(i)
    return items



# the position of start, and the two jails for using elsewhere in the code('s)

starting_position = 0
visiting_jail = 10
jail_position = 41


# Here board_data is a list of dictionaries
# I have the board 'name' along with the spots name that will be printed.
# the 'type' key is for what this spot is
# using my functions above and breaking up the data over multiple lines we have a cleaner code
# i will detail each individual functions data once with comments else hover over the function.

board_data: list[dict[str, Any]] = [
    {'name': 'Go', 'type': 'go', 'salary': 200}, # starting position
    property_func(
        'Mediterranean Ave',    # name of property
        'brown',                # property color
        60,                     # price of property
        50,                     # cost for a new house
        [2, 10, 30, 90, 160]),  # Rent dependent on how many houses
    gendata_func('Community Chest #1', 'chest'), # the first comm chest
    property_func(
        'Baltic Ave',
        'brown',
        60,
        50,
        [4, 20, 60, 180, 320]),
    taxspot_func('Income Tax', 100, 'income_tax'), # no longer use this 100 its calculated in landing
    railroad_func('Reading Railroad', 200, 25), # first railroad name, price, and rent
    property_func(
        'Oriental Ave',
        'grey',
        100,
        50,
        [6, 30, 90, 270, 400]),
    gendata_func('Chance #1', 'chance'), # first chance spot
    property_func(
        'Vermont Ave',
        'grey',
        100,
        50,
        [6, 30, 90, 270, 400]),
    property_func(
        'Connecticut Ave',
        'grey',
        120,
        50,
        [8, 40, 100, 300, 450]),
    gendata_func('Just Visiting / Jail', 'visiting_jail'), #This is where you visit jail
    property_func(
        'St. Charles Place',
        'pink',
        140,
        100,
        [10, 50, 150, 450, 625]),
    utility_func('Electric Company', 150, 5),
    property_func(
        'States Ave',
        'pink',
        140,
        100,
        [10, 50, 150, 450, 625]),
    property_func(
        'Virginia Ave',
        'pink',
        160,
        100,
        [12, 60, 180, 500, 700]),
    railroad_func('Pennsylvania Railroad', 200, 25),
    property_func(
        'St. James Place',
        'orange',
        180,
        100,
        [14, 70, 200, 550, 750]),
    gendata_func('Community Chest #2', 'chest'),
    property_func(
        'Tennessee Ave',
        'orange',
        180,
        100,
        [14, 70, 200, 550, 750]),
    property_func(
        'New York Ave',
        'orange',
        200,
        100,
        [16, 80, 220, 600, 800]),
    gendata_func('Free Parking', 'free_spot'), # free parking - nothing happens :(
    property_func(
        'Kentucky Ave',
        'red',
        220,
        150,
        [18, 90, 250, 700, 875]),
    gendata_func('Chance #2', 'chance'),
    property_func(
        'Indiana Ave',
        'red',
        220,
        150,
        [18, 90, 250, 700, 875]),
    property_func(
        'Illinois Ave',
        'red',
        240,
        150,
        [20, 100, 300, 750, 925]),
    railroad_func('B. & O. Railroad', 200, 25),
    property_func(
        'Atlantic Ave',
        'yellow',
        260,
        150,
        [22, 110, 330, 800, 975]),
    property_func(
        'Ventnor Ave',
        'yellow',
        260,
        150,
        [22, 110, 330, 800, 975]),
    utility_func('Water Works', 150, 5),
    property_func(
        'Marvin Gardens',
        'yellow',
        280,
        150,
        [24, 120, 360, 850, 1025]),
    gendata_func('Go To Jail!', 'go_to_jail'),
    property_func(
        'Pacific Ave',
        'green',
        300,
        200,
        [26, 130, 390, 900, 1100]),
    property_func(
        'North Carolina Ave',
        'green',
        300,
        200,
        [26, 130, 390, 900, 1100]),
    gendata_func('Community Chest #3', 'chest'),
    property_func(
        'Pennsylvania Ave',
        'green',
        320,
        200,
        [28, 150, 450, 1000, 1200]),
    railroad_func('Short Line', 200, 25),
    gendata_func('Chance #3', 'chance'),
    property_func(
        'Park Place',
        'blue',
        350,
        200,
        [35, 175, 500, 1100, 1300]),
    taxspot_func('Luxury Tax', 75, 'luxury_tax'), # second tax is flat rate
    property_func(
        'Boardwalk',
        'blue',
        400,
        200,
        [50, 200, 600, 1400, 1700]),
]

# testing code for my keys and spots
if __name__ == '__main__':
    for i, spot in enumerate(board_data):
        print(i, spot['name'])

    # print(color_pos_func('blue')) # testing out the helper function
