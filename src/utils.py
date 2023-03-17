import os
import platform
from colorama import Fore, Style


def clear_console():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            break
        except ValueError:
            print("Please enter a valid integer.")
    return value

def get_player_names(num_players):
    player_names = []
    for i in range(num_players):
        name = input(f"Enter the name of Player {i + 1}: ").strip()
        player_names.append(name)
    return player_names

def print_board(board, players):
    player_positions = {player.get_position(): player for player in players}
    colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]

    snake_char = "🐍"
    ladder_char = "🪜"

    for row in range(board.size, 0, -1):
        start = (board.size * (row - 1)) + 1
        end = (board.size * row) + 1
        step = 1

        if row % 2 == 0:
            start, end, step = end - 1, start - 1, -1

        for i in range(start, end, step):
            cell = f"{i:3}"

            if i in player_positions:
                player = player_positions[i]
                player_color = colors[players.index(player) % len(colors)]
                cell = f"  {player_color}{player.name[0]}{Style.RESET_ALL}"

            if i in board.snakes:
                print(f"   {Fore.RED}{snake_char}{Style.RESET_ALL}", end=" ")
            elif i in board.ladders:
                print(f"   {Fore.GREEN}{ladder_char}{Style.RESET_ALL}", end=" ")
            else:
                print(f"  {cell}", end=" ")

        print("\n")




