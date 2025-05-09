### Main file that connects Gui and the game ###

# NOTE: Import Section
# Imports required modules for the file
from Gui import *
from Game import *

# Creates a gui using Tkinter for the start menu.
def create_gui() -> tuple:
    """
    Function to create a start screen GUI. This will initialize and run a GUI that acts as the menu for the game.
    Returns:
        tuple: Contains a boolean to start the game and game data for the game if there is any. (Start, Data)
    """

    # Creates the start screen GUI and returns the start bool and game data.
    start_screen = Tk()
    start_screen.attributes("-fullscreen", True)
    start_gui = Gui(start_screen)
    start_screen.mainloop()
    return start_gui.started, start_gui.gameData

def create_game(data) -> bool:
    """
    Function to create the game and run it while passing in game data.
    Parameters:
        data: Game data for the game.
    Returns:
         bool: True if the player died so it takes them to the start screen. False otherwise.
    """

    # Creates the game with any data present and returns True if the player dies.
    game = Game("Deicide", data)
    game.run()
    return game.restart

def main() -> None:
    """
    Main function that runs the gui and the game and stops when the player wants to quit.
    Returns:
        None
    """

    # Loops to create a GUI and Game if the player does not decide to quit willingly.
    while True:
        data = create_gui()

        if data[0]:
            state = create_game(data[1])
            if state:
                continue
            else:
                break
        else:
            break

# Runs the file if it is the main file.
if __name__ == '__main__':
    main()