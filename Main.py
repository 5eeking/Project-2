### Main file that connects Gui and the game ###

from Gui import *
from Game import *

def create_gui():
    start_screen = Tk()
    # start_screen.title("Deicide")
    start_screen.attributes("-fullscreen", True)
    # start_screen.resizable(width=False, height=False)
    start_gui = Gui(start_screen)
    start_screen.mainloop()
    return start_gui.started, start_gui.gameData

def create_game():
    game = Game("Deicide")
    game.run()
    return False

def main():
    while True:
        data = create_gui()

        print(data)

        if data[0]:
            state = create_game()
            if state:
                continue
            else:
                break
        else:
            break

if __name__ == '__main__':
    main()