
# NOTE: Import Section
# Imports required modules for the file
import pygame as py
from SpriteSheet import SpriteSheet
import random as rand
import os

class Upgrades:

    def __init__(self, x, y, width, height, chest_type) -> None:
        """
        Initializes the required variables for the upgrade.
        Parameters:
            x: the x coordinate of the upgrade.
            y: the y coordinate of the upgrade.
            width: the width of the upgrade.
            height: the height of the upgrade.
            chest_type: the chest type of the upgrade. (Damage, Health, Protection
        """

        # NOTE: Upgrade Initializer
        # Initializes the variables needed for the upgrades.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dmg_up = 0
        self.health_up = 0
        self.prot_up = 0

        # Sets up the upgrade sprite sheet and variables
        self.sprite_sheet_image = py.image.load(f"sprites{os.sep}chests.png").convert_alpha()
        self.sprite_sheet = SpriteSheet(self.sprite_sheet_image)
        self.chest_type = chest_type
        self.chest_list = []
        self.chest_steps = 4

        # Gets all the sprites for each upgrade type.
        step_counter = 0
        for _ in range(self.chest_steps):
            self.chest_list.append(self.sprite_sheet.get_image(step_counter, 4, self.width, self.height, 2, (100, 255, 155)))
            step_counter += 1

        # Determines the upgrade type and gets the upgrade amount.
        if self.chest_type == "Rand":
            rand_upgrade = rand.randint(1, 3)
            if rand_upgrade == 1:
                self.dmg_up = 3
            elif rand_upgrade == 2:
                self.health_up = 10
            elif rand_upgrade == 3:
                self.prot_up = 5
        elif self.chest_type == "Damage":
            self.dmg_up = 5
        elif self.chest_type == "Health":
            self.health_up = 15
        elif self.chest_type == "Protection":
            self.prot_up = 10

    def collect(self, player) -> None:
        """
        Collects the upgrade for the player by adding the upgrade to the player.
        Parameters:
            player: the player object.
        Returns:
            None
        """

        # Adds the upgrade to the player when collected.
        player.damage += self.dmg_up
        player.health_max += self.health_up
        player.health += self.health_up
        player.protection += self.prot_up

    def update(self, display, display_scroll ) -> None:
        """
        Updates the upgrade chest onto the screen.
        Parameters:
            display: the display object.
            display_scroll: the display scroll for the screen.
        Returns:
            None
        """

        # Updates the chest on the screen for the corresponding type.
        if self.chest_type == "Rand":
            display.blit(self.chest_list[0], (self.x - display_scroll[0], self.y - display_scroll[1]))
        elif self.chest_type == "Damage":
            display.blit(self.chest_list[2], (self.x - display_scroll[0], self.y - display_scroll[1]))
        elif self.chest_type == "Health":
            display.blit(self.chest_list[3], (self.x - display_scroll[0], self.y - display_scroll[1]))
        elif self.chest_type == "Protection":
            display.blit(self.chest_list[1], (self.x - display_scroll[0], self.y - display_scroll[1]))