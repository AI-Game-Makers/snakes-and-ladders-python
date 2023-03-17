import random
from src.board import Board
from src.player import Player
from src.utils import clear_console, get_integer_input, get_player_names, print_board

class Game:
    def __init__(self, num_players, board_size=10, num_snakes=5, num_ladders=5):
        self.num_players = num_players
        self.board = Board(board_size, num_snakes, num_ladders)
        player_names = get_player_names(num_players)
        self.players = [Player(name) for name in player_names]

    def play(self):
        clear_console()
        print("Welcome to Snakes and Ladders!")
        print("The first player to reach the final square wins!")
        input("Press Enter to start...")

        while True:
            for player in self.players:
                clear_console()
                print_board(self.board, self.players)

                print(f"\n{player}'s turn")
                input("Press Enter to roll the dice...")
                roll = random.randint(1, 6)
                print(f"{player} rolled a {roll}.")

                new_position = self.board.move(player.get_position(), roll)
                print(f"{player} moved from {player.get_position()} to {new_position}.")
                player.set_position(new_position)

                if self.board.is_winning_position(new_position):
                    clear_console()
                    print_board(self.board, self.players)
                    print(f"\nCongratulations, {player}! You won!")
                    return

                input("Press Enter to continue...")

def main():
    num_players = get_integer_input("Enter the number of players (2-4): ")
    while num_players not in range(2, 5):
        print("Please enter a valid number of players.")
        num_players = get_integer_input("Enter the number of players (2-4): ")

    game = Game(num_players)
    game.play()

if __name__ == "__main__":
    main()