### Gui for start menu using tkinter ###

from tkinter import *
from SaveLoadSystem import SaveLoadSystem
import os
from Game import Game

class Gui:
    def __init__(self, screen) -> None:
        """
        Initializes the GUI and puts all the elements on the screen.
        Parameters:
             screen: This is the screen that everything is put onto.
        """

        # Creates the variables for the gui and outside use.
        self.save_load_system = SaveLoadSystem(".txt", "gameData")
        self.continued = True if self.save_load_system.check_for_file("player_data") and self.save_load_system.check_for_file("game_data") else False
        self.gameData = self.save_load_system.load_game_data(["player_data", "game_data"], [[], []])
        self.started = False
        self.screen = screen

        # Makes the screen background light blue.
        self.screen.config(bg="Light Blue")

        # Title of the game put onto the screen.
        self.frame_one = Frame(self.screen, bg = "Light Blue")
        self.label_one = Label(self.frame_one, text = "DEICIDE", font = ("Baskerville Old Face", 100, "bold"), bg = "Light Blue")
        self.label_one.pack(anchor = "n", pady = 30)
        self.frame_one.pack(anchor = "n")

        # Button to start a new game.
        self.frame_two = Frame(self.screen, bg = "Light Blue")
        self.button_one = Button(self.frame_two, text = "START", font = ("Baskerville Old Face", 45, "bold"),
                                 bg = "light gray", borderwidth = 5, width = 13, command = self.start_new)
        self.button_one.pack(anchor = "n", pady = 10)
        self.frame_two.pack(anchor = "n")

        # Button to continue the previously played game.
        self.frame_three = Frame(self.screen, bg = "Light Blue")
        self.button_bonus = Button(self.frame_three, text="CONTINUE", font=("Baskerville Old Face", 45, "bold"),
                                 bg="light gray", borderwidth=5, width=13, command=self.start_continue)
        self.button_bonus.pack(anchor="n", pady=10)
        self.frame_three.pack(anchor="n")

        # Disables the continue button if there is no pre-existing file.
        if not self.continued:
            self.button_bonus.configure(state=DISABLED)

        # Button to exit the GUI.
        self.frame_four = Frame(self.screen, bg = "Light Blue")
        self.button_three = Button(self.frame_four, text = "EXIT", font = ("Baskerville Old Face", 45, "bold"),
                                   bg = "light gray", borderwidth = 5, width = 13, command = screen.destroy)
        self.button_three.pack(anchor = "n", pady = 10)
        self.frame_four.pack(anchor = "n")

    def start_new(self) -> None:
        """
        Starts a new game when the player presses the start button.
        Returns:
            None
        """

        # Starts the game and resets the game data.
        self.started = True
        self.gameData = [[], []]
        self.screen.destroy()

    def start_continue(self) -> None:
        """
        Starts a pre-existing game when the player presses the continue button.
        Returns:
            None
        """

        # Starts the game with pre-existing game data.
        self.started = True
        self.screen.destroy()