from random import randint

# global variables
HIT = []
MISS = []


class Battleship:
    """
    Sets the size of the board, number of ships, user name, and board type.
    Also calls the random_ships method to set ships.
    """

    def __init__(self, board_size, num_ships, user_name):
        self.board_size = board_size
        self.num_ships = num_ships
        self.user_name = user_name
        self.ships = self.random_ships()
        self.hits = []  # Initialize hits as a list
        self.misses = []

    def random_ships(self):
        """
        Sets the ships to the board
        """
        ships = []
        while len(ships) < self.num_ships:
            ship_row = randint(0, self.board_size - 1)
            ship_col = randint(0, self.board_size - 1)
            ship_coord = (ship_row, ship_col)

            # Make sure the ship is not already in the list
            if ship_coord not in ships:
                ships.append(ship_coord)
            
        return ships

    def print_board(self, show_ships=False):
        """
        Prints out the boards to terminal and checks if it's HIT or MISS.
        """
        print(f" {self.user_name}'s board \n")
        print("   0  1  2  3  4")
        for x in range(self.board_size):
            row = ""
            for y in range(self.board_size):
                coord = (x, y)
                symb = " . "
                if coord in self.hits:
                    symb = " H "
                elif coord in self.misses:
                    symb = " M "
                row = row + symb
            print(x, row)

    def play_turn(self, row, col):
        coord = (row, col)
        if coord in self.ships:
            self.hits.append(coord)
            self.ships.remove(coord)
            print("HIT!")
        else:
            self.misses.append(coord)
            print("MISS!")


def start_game():
    """
    Starting the game with introduction and rules.
    Setting the size of game board and the number of ships.
    Lets user put in name before start.
    """

    board_size = 5
    num_ships = 3
    print("-+" * 20)
    print("Welcome to Sea Battle! \n")
    print(f"Board size: {board_size}. Number of ships: {num_ships}")
    print("Goal: Sink all of your opponent's ships. \n")
    print("Player ships = S")
    print("HIT = H")
    print("MISS = M \n")
    
    print("Rules: ")
    print("- Player starts with guessing column and row.")
    print("- The column and row guess should be between 0-4")
    print("- Top left corner is row: 0, col: 0.")
    print("- Game ends when you have hit all the ships!")
    print("-+" * 20)
    user_name = input("Please enter your name before start: \n")

    return user_name


def get_ship_guess():
    """
    Getting ship guesses from user and validate the coordinates.
    """

    guess_row = input("Please enter a row 0-4: \n")
    while guess_row not in ['0', '1', '2', '3', '4']:
        print("Please enter a valid row.")
        guess_row = input("Please enter a row 0-4: \n")

    guess_col = input("Please enter a col 0-4: \n")
    while guess_col not in ['0', '1', '2', '3', '4']:
        print("Please enter a valid column.")
        guess_col = input("Please enter a col 0-4: \n")
    return int(guess_row), int(guess_col)


def main():
    """
    Calling the functions to run the game
    """

    board_size = 5
    num_ships = 3
    user_name = start_game()

    player_game = Battleship(board_size, num_ships, user_name)

    print(player_game.ships)  # Print the player ships coordinates for testing
    turns = 5
    while len(player_game.ships) > 0:
        player_game.print_board()
        row, col = get_ship_guess()
        player_game.play_turn(row, col)
        turns -= 1

        if len(player_game.ships) == 0:
            print("Congratulations, you sank all of the ships!")
        elif turns == 0:
            print("Game over!")
            break


main()

