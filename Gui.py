### Gui for start menu using tkinter ###

from tkinter import *
import os
from Game import Game

class Gui:
    def __init__(self, screen):
        self.continued = True if os.path.isfile(f"gameData{os.sep}gameData.txt") else False
        self.gameData = []
        self.started = False
        self.screen = screen

        self.screen.config(bg="Light Blue")

        # Title of the game put onto the screen
        self.frame_one = Frame(self.screen, bg = "Light Blue")
        self.label_one = Label(self.frame_one, text = "DEICIDE", font = ("Baskerville Old Face", 100, "bold"), bg = "Light Blue")
        self.label_one.pack(anchor = "n", pady = 30)
        self.frame_one.pack(anchor = "n")

        # Button to start a new game.
        self.frame_two = Frame(self.screen, bg = "Light Blue")
        self.button_one = Button(self.frame_two, text = "START", font = ("Baskerville Old Face", 45, "bold"),
                                 bg = "light gray", borderwidth = 5, width = 13, command = self.start)
        self.button_one.pack(anchor = "n", pady = 10)
        self.frame_two.pack(anchor = "n")

        # Button to continue the previously played game.
        self.frame_three = Frame(self.screen, bg = "Light Blue")
        self.button_bonus = Button(self.frame_three, text="CONTINUE", font=("Baskerville Old Face", 45, "bold"),
                                 bg="light gray", borderwidth=5, width=13, command=self.start)
        self.button_bonus.pack(anchor="n", pady=10)
        self.frame_three.pack(anchor="n")

        if not self.continued:
            self.button_bonus.configure(state=DISABLED)

        # TODO: Add a command to the button
        self.frame_four = Frame(self.screen, bg = "Light Blue")
        self.button_three = Button(self.frame_four, text = "EXIT", font = ("Baskerville Old Face", 45, "bold"),
                                   bg = "light gray", borderwidth = 5, width = 13, command = screen.destroy)
        self.button_three.pack(anchor = "n", pady = 10)
        self.frame_four.pack(anchor = "n")

    def start(self):
        self.started = True
        self.screen.destroy()