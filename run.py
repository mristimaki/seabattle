from random import randint

def start_game():
    """
    Starting the game with introduction and rules.
    Setting the size of game board and the number of ships.
    Lets user put in name before start.
    """

    board_size = 5
    num_ships = 5
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
    

start_game()