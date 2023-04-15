from random import randint


def get_ship_guess():
    """
    Getting ship guesses from user and validate the coordinates.
    """
    
    guess_row = input("Please enter a row 0-4: ")
    while guess_row not in '01234':
        print("Please anter a valid row.")
        guess_row = input("Please enter a row 0-4: ")

    guess_col = input("Please enter a col 0-4: ")
    while guess_col not in '01234':
        print("Please enter a valid column.")
        guess_col = input("Please enter a col 0-4: ")
    return int(guess_row), int(guess_col)



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
    user_name = input("Please enter your name before start: ")

    def player_board():
        print(f"{user_name}'s board")
        print("   0  1  2  3  4")
        for x in range(5):
            print(x, " . "*5)
        print("\n")

    def computer_board():
        print("Computer's board")
        print("   0  1  2  3  4")
        for x in range(5):
            print(x, " . "*5)
        print("\n")

    player_board()
    computer_board()
    

def main():
    """
    Calling the functions to run the game
    """
    start_game()
    get_ship_guess()

main()