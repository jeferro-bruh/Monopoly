"""
playing_cards.py
Jethro AA
Made Oct. 18th 2026

Making the playing cards! We will have chance and chest cards here.
The theme of the cards is pretty simple, usually just moving back or forwards,
gaining or losing money, or going to jail. I plan on making it a little more fun later.
"""

# These cards have 6 main actions:
# add_money / remove_money - both positive to prevent double negative use to remove set value
# move_to  / move_backwards - all dictate how you will move once card is drawn
# go_to_jail - simply puts you in jail position, monopoly_board.py has jail logic
# I have leave_jail too but undecided if im gonna keep this card.


# importing Any from typing so I can stop pylance from yelling at me.
from typing import Any
# using random here will be useful for shuffling my deck easily.
import random
# we can use jail position for card logic
from board_data import jail_position, board_data

# My first function is simply to make the cards in a different order each time.
def shuffle_cards() -> None:
    """
    A simple function to shuffle the cards using random.shuffle. Should be called
    once at the start of the game to make my dictionaries random (like shuffling cards).
    """
    random.shuffle(chance_cards)
    random.shuffle(chest_cards)

# This makes it feel more like a real card deck via looping order.
def draw_card(cards: list[dict[str, Any]]) -> dict[str, Any]:
    """
    A function to draw your card that can be called when the player lands on
    a position that gives a card like community chest, or chance.

    Parameters
    ----------
    cards : list[dict[str, Any]]
        The parameter here lets you draw either chance or chest then you can 
        access the data as needed. 

    Returns
    -------
    dict[str, Any]
        Returns the card we just drew and moves the value to the back
        so we can have a looping card deck.
    """
    # pop(0) lets me remove the top card.
    given = cards.pop(0)
    cards.append(given) # moves the popped card to the back.
    return given


# activate_card function will be my logic for actually using a card.
def activate_card(
        card: dict[str, Any],
        player: int,
        positions: list[int],
        money: list[int]) -> None:
    action = card['action']
    value = card['value']


    if action == 'add_money':
        money[player] += value
    elif action == 'remove_money':
        money[player] -= value
    elif action == 'go_to_jail':
        positions.pop(player)
        positions.insert(player, jail_position)

    elif action == 'move_to':
        if value < positions[player]:
            money[player] += board_data[0]['salary']
        positions[player] = value

    elif action == 'move_backwards':
        positions[player] = (positions[player] - value) % 40



# The chance cards are here using 'text', 'action' and 'value'
# I want to add more later but thing this is an okay start.
chance_cards: list[dict[str, Any]] = [
    {
        'text': 'Advance to "Go"',
        'action': 'move_to',
        'value': 0},
    {
        'text': 'Advance to Illinois Ave',
        'action': 'move_to',
        'value': 24},
    {
        'text': 'Advance to St. Charles Place',
        'action': 'move_to',
        'value': 11},
    {
        'text': 'Advance to Electric Company',
        'action': 'move_to',
        'value': 12},
    {
        'text': 'Advance to Reading Railroad',
        'action': 'move_to',
        'value': 5},
    {
        'text': 'Bank pays you dividend of $50.',
        'action': 'add_money',
        'value': 50},
    # {
    #     'text': 'Get out of Jail Free',
    #     'action': 'leave_jail',
    #     'value': jail_position},
    {
        'text': 'Go back 3 Spaces',
        'action': 'move_backwards',
        'value': 3},
    {
        'text': 'Go to Jail',
        'action': 'go_to_jail',
        'value': jail_position},
    {   # needs a secondary action to check if have hotel ( no hotels yet)
        'text': 'Pay repairs on properties. Pay $25 per house',
        'action': 'remove_money',
        'value': 25},
]

# my chest cards are here with the same format as the chance cards but different texts
chest_cards: list[dict[str, Any]] = [
    {
        'text': 'Advance to "Go"',
        'action': 'move_to',
        'value': 0},

    {
        'text': 'Doctor\'s fees',
        'action': 'remove_money',
        'value': 50},
    {
        'text': 'Bank error. Collect $200',
        'action': 'add_money',
        'value': 200},
    # {
    #     'text': 'Get out of Jail Free',
    #     'action': 'leave_jail',
    #     'value': 10},
    {
        'text': 'Go to Jail',
        'action': 'go_to_jail',
        'value': jail_position},
    {
        'text': 'Income tax refund. Collect $20',
        'action': 'add_money',
        'value': 20},
    {
        'text': 'It\'s your birthday! Collect $10 dollars',
        'action': 'add_money',
        'value': 10},
    {
        'text': 'You are asked to fund public schools',
        'action': 'remove_money',
        'value': 100},
    {
        'text': 'You inherit $100 from your grunkle Stan',
        'action': 'add_money',
        'value': 100},
    {
        'text': 'A time traveler asks for $20 worth of bitcoin',
        'action': 'remove_money',
        'value': 20},
]

# testing out my functions
if __name__ == '__main__':
    positions = [0, 0, 0 ,0]
    money = [100, 100, 100, 100]
    shuffle_cards()
    print(money)
    print(positions)
    print(draw_card(chance_cards))
    activate_card(draw_card(chance_cards), 1, positions, money)
    print(money)
    print(positions)
