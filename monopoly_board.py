"""
monopoly_board.py
Orion Stiehm

Making the board, dice and player movement.
"""
import random
import time


def open_menu() -> list[str]:
    """
    _summary_

    It is used at the start to generate the list of icons and player count
    ----------
    input_position : list[int]
        _description_

    Returns
    -------
    list[str]
        _description_

    Askes how many playeres there will be, then asks what icons they want
    """
    print("""


Big Cool Monopoly Logo


""")
    question: int = 0
    players: str
    num_players: int = 0
    character_pieces: list[str] = ["!","@","#","$","%","&","*","+","="]
    final_icons: list[str] = []
    choice: str
    n: int = 0
    i: int = 0
    while question != 5:
        question += 1
        if question == 1:
            players = input("\nHow many players are playing?\n>")
            if players == "2":
                num_players = 2
            elif players == "3":
                num_players = 3
            elif players == "4":
                num_players = 4
            else:
                question -= 1
                print("\nNot valid answer")
        if question == 2:
            while len(final_icons) < num_players:
                n += 1
                print(f"\n\n   {character_pieces[0]}   {character_pieces[1]}" +
                      f"   {character_pieces[2]}   {character_pieces[3]}  " +
                      f" {character_pieces[4]}   {character_pieces[5]} " +
                    f"  {character_pieces[6]}   {character_pieces[7]}   {character_pieces[8]}")
                for i in range(1, 10 - len(final_icons)):
                    print(f"   {i}", end = "")
                choice = input(f"\n\nWhat icon does player {n} want?\n>")
                if choice.isdigit() is True:
                    choice_num = int(choice)
                    if choice_num < 10 - len(final_icons) and choice_num != 0:
                        final_icons.append(character_pieces.pop(choice_num - 1))
                        character_pieces.append(" ")
                    else:
                        print("\nNot valid answer")
                        n -= 1
                else:
                    print("\nNot valid answer")
                    n -= 1
    return final_icons


def roll_dice() -> list[int]:
    """
    _summary_

    IT provides the odds of two D6s and displays the rolls
    Parameters
    ----------
    input_position : list[int]
        _description_

    Returns
    -------
    int
        _description_
        Generates two random numbers then displays them both then adds them
    """
    dice: list[int] = [random.randint(1,6),random.randint(1,6)] # Both dice rolls
    time.sleep(0.7)
    print_dice(dice[0]) # Display dice 1
    time.sleep(1.2)
    print_dice(dice[1]) # Display dice 2
    time.sleep(3)
    return dice


def print_dice(roll: int) -> None:
    """
    _summary_
    Given a 1-6 int it will display that dice face
    Parameters
    ----------
    roll : int
        _description_
    """
    print("\n\x1b[0;30;47m+=========+\x1b[0m")
    if roll > 3: # Prints if its a 4 5 or 6
        print("\x1b[0;30;47m|  0   0  |\x1b[0m")
    elif roll > 1: # Prints if its 3 or a 2
        print("\x1b[0;30;47m|      0  |\x1b[0m")
    else: # Prints if its a 1
        print("\x1b[0;30;47m|         |\x1b[0m")
    if roll == 6: # Prints if its a 6
        print("\x1b[0;30;47m|  0   0  |\x1b[0m")
    elif roll == 2 or roll == 4: # Prints if its a 2 or a 4
        print("\x1b[0;30;47m|         |\x1b[0m")
    else: # Prints if its a 1 3 or 5
        print("\x1b[0;30;47m|    0    |\x1b[0m")
    if roll > 3: # Prints if its a 4 5 or 6
        print("\x1b[0;30;47m|  0   0  |\x1b[0m")
    elif roll > 1: # Prints if its a 3 or a 2
        print("\x1b[0;30;47m|  0      |\x1b[0m")
    else: # Prints if its a 1
        print("\x1b[0;30;47m|         |\x1b[0m")
    print("\x1b[0;30;47m+=========+\x1b[0m")



def moving_player(player: int, movement: int, positions: list[int],
                  player_symbols: list[str]) -> list[int]:
    """
    _summary_

    Moves a player through the board with a givin distance one space at a time
    Parameters
    ----------
    player : int
        _description_
    movement : int
        _description_
    positions : list[int]
        _description_
    player_symbols : list[str]
        _description_

    Returns
    -------
    list[int]
        _description_
    """
    n: int
    total_players = len(player_symbols)
    final_positions: list[int] = positions # The final positions of the players after this
    board_position: list[str] = [" "] * 42 # The graphic that'll be shown in each spot in the board
    for n in range(0,movement):
        board_position = [" "] * 42
        positions[player] += 1 # Adds one to the position
        if positions[player] == 40: # Checks if they should be looped on the board
            positions[player] = 0
            #money[player] += 200
        final_symbols: list[str] = player_display(positions, player_symbols, total_players)
        for n in range(0,total_players): #Replaces the player icon on their space on the list
            board_position[positions[n]] = final_symbols[n]
        print_board(board_position)
        time.sleep(0.5)
    return final_positions

def player_display(player_spots: list[int], choice_symbol: list[str], players: int) -> list[str]:
    """
    _summary_
    It takes the players positions and outputs what their symbol should be
    Parameters
    ----------
    player_spots : list[int]
        _description_
    choice_symbol : list[str]
        _description_
    If players are on the same space then its just a number, otherwise their symbol
    Returns
    -------
    list[str]
        _description_
    """
    final_symbol: list[str] = ["X", "X", "X", "X"] # Sets their default icon
    players_together: int = 0 # A variable to check how many players are in one space
    for i in range(0,players): # Switching for player i
        players_together = 0
        for n in range(0,players): # Switching for player n
            if player_spots[i] == player_spots[n]: # Check if player i is on player n's space
                players_together += 1
        if players_together == 1:
            final_symbol[i] = choice_symbol[i]
        else:
            final_symbol[i] = f"{players_together}"
    return final_symbol


def print_board(player_spot: list[str]) -> None: # Honestly i'm just saying it prints the board
    """
    _summary_
    Print the Monopoly board with the player on it

    Parameters
    ----------
    player_spot : dict[int, str]
    """
    n: int = 0
    print("\n" * 50)
    print("\n\x1b[5;30;42m+" + "=" *86 + "+\x1b[0m")
    print("\x1b[5;30;42m|           |" + "      |" * 9 + "           |\x1b[0m")

    print(f"\x1b[5;30;42m|   {player_spot[20]}       |", end = "")
    for n in range(0,9):
        print(f"  {player_spot[21+n]}   |", end = "")
    print(f"       {player_spot[30]}   |\x1b[0m")
    print("\x1b[5;30;42m|           |" + "      |" * 9 + "           |\x1b[0m")
    print("\x1b[5;30;42m|           |", end = "")
    for n in range(1,10):
        if n == 1 or n == 4 or n == 3:
            print("\x1b[5;30;41m      \x1b[5;30;42m" + "|", end = "")
        elif n == 9 or n == 7 or n == 6:
            print("\x1b[5;30;43m      \x1b[5;30;42m" + "|", end = "")
        elif n == 8:
            print("WATER |", end = "")
        elif n == 5:
            print(" RAIL |", end = "")
        elif n == 2:
            print("  ??  |", end = "")
        else:
            print("      |", end = "")
    print("           |\x1b[0m")
    print("\x1b[5;30;42m+===========+" + "======+" * 9 + "===========|\x1b[0m")
    for n in range(0,9):
        if n < 2 or n == 3:
            print("\x1b[5;30;42m|         \x1b[6;31;43m\033[1m##\x1b[5;30;42m|" + " " * 62 +
                  "|\x1b[0;30;47m  \x1b[5;30;42m         |\x1b[0m")
            print(f"\x1b[5;30;42m|   {player_spot[19-n]}     \x1b[6;31;43m\033[1m##\x1b[5;30;42m|" +
                  " " * 62 + "|\x1b[0;30;47m  \x1b[5;30;42m" +
                  f"     {player_spot[31+n]}   |" + "\x1b[0m")
        elif n == 6 or n == 8:
            print("\x1b[5;30;42m|         " + "\x1b[0;30;45m" + "  " + "\x1b[5;30;42m" +
                  "|" + " " * 62 + "\x1b[5;30;42m|", end = "")
            print("\x1b[0;30;44m  \x1b[5;30;42m         |" + "\x1b[0m")
            print(f"\x1b[5;30;42m|   {player_spot[19-n]}     " +
                  "\x1b[0;30;45m" + "  " + "\x1b[5;30;42m" + "|" +
                  " " * 62 + "|", end = "")
            print(f"\x1b[0;30;44m  \x1b[5;30;42m     {player_spot[31+n]}   |" + "\x1b[0m")
        elif n == 5:
            print("\x1b[5;30;42m|         " + "\x1b[0;30;45m" + "  " + "\x1b[5;30;42m" +
                  "|" + " " * 62 + "|??         |\x1b[0m")
            print(f"\x1b[5;30;42m|   {player_spot[19-n]}     " + "\x1b[0;30;45m  \x1b[5;30;42m" +
                  "|" + " " * 62 + f"|??     {player_spot[31+n]}   |\x1b[0m")
        elif n == 4:
            print("\x1b[5;30;42m|         RA|" + " " * 62 + "|RA         |\x1b[0m")
            print(f"\x1b[5;30;42m|   {player_spot[19-n]}     IL|" + " " * 62 +
                  f"|IL     {player_spot[31+n]}   |\x1b[0m")
        elif n == 2:
            print("\x1b[5;30;42m|         CH|" + " " * 62 + "|CH         |\x1b[0m")
            print(f"\x1b[5;30;42m|   {player_spot[19-n]}     ST|" + " " * 62 +
                  f"|ST     {player_spot[31+n]}   |\x1b[0m")
        elif n == 7:
            print("\x1b[5;30;42m|         EL|" + " " * 62 + "|TA         |\x1b[0m")
            print(f"\x1b[5;30;42m|   {player_spot[19-n]}     EC|" + " " * 62 +
                  f"|X      {player_spot[31+n]}   |\x1b[0m")
        if n != 8:
            print("\x1b[5;30;42m|===========+" + " " * 62 + "+===========|\x1b[0m")
        else:
            print("\x1b[5;30;42m+===========+" + "======+" * 9 + "===========|\x1b[0m")
    print(f"\x1b[5;30;42m|      | {player_spot[41]}  |", end = "")
    for n in range(1,10):
        if n < 3 or n == 4:
            print("\x1b[5;30;46m      \x1b[5;30;42m" + "|", end = "")
        elif n == 9 or n == 7:
            print("\x1b[5;30;40m      \x1b[5;30;42m" + "|", end = "")
        elif n == 8:
            print("CHEST |", end = "")
        elif n == 6:
            print(" TAX  |", end = "")
        elif n == 5:
            print(" RAIL |", end = "")
        elif n == 3:
            print("  ??  |", end = "")
        else:
            print("      |", end = "")
    print("           |\x1b[0m")
    print("\x1b[5;30;42m|      |____|" + "      |" * 9 + "   GO      |\x1b[0m")
    print(f"\x1b[5;30;42m|   {player_spot[10]}       |", end = "")
    for n in range(0,9):
        print(f"  {player_spot[9-n]}   |", end = "")
    print(f"       {player_spot[0]}   |\x1b[0m")
    print("\x1b[5;30;42m|           |" + "      |" * 9 + "           |\x1b[0m")
    print("\x1b[5;30;42m+" + "=" *86 + "+\x1b[0m")

def main() -> None:
    """
    The main function
    """
    player_positions: list[int] = [0, 0, 0, 0] # Used for each player in the list how far they are
    jail_timer: list[int] = [0, 0, 0, 0] # To see how many turns they've been in jail
    players_choice_symbol: list[str] = open_menu() # Their player icon
    player_count: int = len(players_choice_symbol)
    players_turn: int = -1 # cycles from 0 to 3, starts at -1 because it keeps getting +1
    rolls: list[int] # A list of both rolls given from roll_dice()
    doubles: int = 1 # used to count the doubles of rolling
    while True:
        players_turn += 1 # increment the turn
        if players_turn == player_count: # loops the cycle
            players_turn = 0
        if jail_timer[players_turn] == 3:
            player_positions[players_turn] = 10
        if player_positions[players_turn] == 41:
            jail_timer[players_turn] += 1
            action: str = input(f"""
             It's player {players_turn + 1}s turn, your in jail, what do you want to do?:
            \n1) Roll dice to get out\n2) Pay your way out\n>""") # The menu for if your in jail
            if action == "1": # If you pick option 1
                rolls = roll_dice() # gets two 1-6 ints and saves to rolls
                if rolls[0] == rolls[1]: #Check if double
                    player_positions[players_turn] = 10
                    player_positions = moving_player(players_turn, rolls[0] + rolls[1],
                                          player_positions, players_choice_symbol)
                    #landing_thing()
            elif action == "2": # If you pick option 2
                #money_var -= 50
                player_positions[players_turn] = 10 # sets them outside the jail
                time.sleep(1)
            else: # It the didn't type anything givin
                print("\nPlease input one of the numbers\n")
                jail_timer[players_turn] -= 1
                players_turn -= 1
        else:
            action: str = input(f"""
                  It's player {players_turn + 1}s turn, what do you want to do?:
            \n1) Roll dice\n2) Buy houses\n3) Mortgage\n>""") # Normal turn menu
            if action == "1": # If you pick option 2
                doubles = 0 # Resets doubles to 0
                while doubles != 1:
                    doubles += 1 # Adds one to double, so if no double is gotten it exits the loop
                    rolls = roll_dice()
                    if rolls[0] == rolls[1]:
                        doubles += 1
                        print("\nDOUBLES!")
                        time.sleep(2)
                    else:
                        doubles = 1 # Sets doubles to one to end the loop
                    if doubles == 6: # Doubles grows by 2 for every double, so if 6, then 3 doubles
                        print("\nJailed for your third double")
                        player_positions[players_turn] = 41 # Sets them in jail
                        break
                    player_positions = moving_player(players_turn, rolls[0] + rolls[1],
                                         player_positions, players_choice_symbol)
                    #landing_thing()
            elif action == "2": # If you pick option 2
                #buy_house()
                pass
            elif action == "3": # If you pick option 3
                #mortgage()
                pass
            else:
                print("\nPlease input one of the numbers\n")
                players_turn -= 1

if __name__ == "__main__":
    main()
