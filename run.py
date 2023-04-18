from random import randint

# global variables
HIT = []
MISS = []


class Battleship:
    """
    Sets the size of the board, number of ships, user name and board type.
    """

    def __init__(self, board_size, num_ships, user_name, board_type):
        self.board_size = board_size
        self.num_ships = num_ships
        self.user_name = user_name
        self.board_type = board_type
        self.ships = self.random_ships()  # Call the random_ships method to set ships
        self.guess = []

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
    print("Rules: ")
    print("- Player starts with guessing column and row.")
    print("- The column and row guess should be between 0-4")
    print("- Top left corner is row: 0, col: 0.")
    print("- You will be informed if you got a 'Hit' or 'Miss'")
    print("- Computer turn.")
    print("- New turn.")
    print("-+" * 20)
    user_name = input("Please enter your name before start: \n")

    def player_board():
        """
        Prints out the players board to terminal
        """
        print(f"{user_name}'s board")
        print("   0  1  2  3  4")
        for x in range(5):
            print(x, " . "*5)

    def computer_board():
        """
        Prints out the game board to terminal
        """
        print("Computer's board")
        print("   0  1  2  3  4")
        for x in range(5):
            print(x, " . "*5)

    player_board()
    print("\n")
    computer_board()


def get_ship_guess():
    """
    Getting ship guesses from user and validate the coordinates.
    """

    guess_row = input("Please enter a row 0-4: ")
    while guess_row not in ['0', '1', '2', '3', '4']:
        print("Please anter a valid row.")
        guess_row = input("Please enter a row 0-4: ")

    guess_col = input("Please enter a col 0-4: ")
    while guess_col not in ['0', '1', '2', '3', '4']:
        print("Please enter a valid column.")
        guess_col = input("Please enter a col 0-4: ")
    return int(guess_row), int(guess_col)


def main():
    """
    Calling the functions to run the game
    """

    board_size = 5
    num_ships = 3
    user_name = input("Please enter your name before start: \n")
    game = Battleship(board_size, num_ships, user_name, "player")
    print(game.ships)  # Print the ships' coordinates for testing purposes
    start_game()
    get_ship_guess()

main()