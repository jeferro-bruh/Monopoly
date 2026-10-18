"""
playing_cards.py
Jethro AA
Made Oct. 18th 2026

Making the playing cards! We will have chance and chest cards here.
The theme of the cards is pretty simple, usually just moving back or forwards,
gaining or losing money, or going to jail. I plan on making it a little more fun later.
"""
# importing Any from typing so I can stop pylance from yelling at me.
# using random here will be useful for shuffling my deck easily.
from typing import Any
import random

# My first function is simply to make the cards in a different order each time.
def shuffle_cards() -> None:
    """
    A simple function to shuffle the cards using random.shuffle. Should be called
    one at the start of the game to make my dictionaries random (like shuffling cards).
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

# The chance cards are here using 'text', 'action' and 'value'
# I want to add more later but thing this is an okay start.
chance_cards: list[dict[str, Any]] = [
    {'text': 'Your rich distant relative left you money!', 'action': 'add_money', 'value': 2},
    {'text': 'You fell down the stairs, pay hospital bill.', 'action': 'lose_money', 'value': 2},
    {'text': 'Free bus pass: move 4 spots forward.', 'action': 'move_forward', 'value': 4},
    {'text': 'You have been arrested! Go to jail', 'action': 'go_to_jail', 'value': 0}
]

# my chest cards are here with the same format as the chance cards but different texts
chest_cards: list[dict[str, Any]] = [
    {'text': 'You found money on the side of the road!', 'action': 'add_money', 'value': 2},
    {'text': 'Pay the bank service fees.', 'action': 'lose_money', 'value': 2},
    {'text': 'Advance to go', 'action': 'move_to', 'value': 0},
    {'text': 'You were jailed for embezzlement! Go to Jail ', 'action': 'go_to_jail', 'value': 0}
]

# testing out my functions
if __name__ == '__main__':
    shuffle_cards()
    for i in range(1):
        print(draw_card(chance_cards)['text'])
