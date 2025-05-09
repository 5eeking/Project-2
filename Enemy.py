### File to create the enemies ###

# NOTE: Import Section
# Imports required modules for the file
import pygame as py
from Logic import *
from SpriteSheet import SpriteSheet
from HealthBar import HealthBar
import random as rand
import os

# Enemy class to create enemy entities.
class Enemy:
    ANIMATION_COOLDOWN = 175
    def __init__(self, x, y, speed, width, height, enemy_type, health, damage, point_amount, display_scroll, screen) -> None:
        """
        Initializes the enemy variables, position, and animations for each enemy type.
        Parameters:
            x: x position of the enemy.
            y: y position of the enemy.
            speed: speed of the enemy.
            width: width of the enemy.
            height: height of the enemy.
            enemy_type: type of enemy (Monster, Skeleton, Hero).
            health: health of the enemy.
            damage: damage the enemy does.
            point_amount: point amount the enemy gives on death.
            display_scroll: extra position to move the enemy on the screen based on player movement.
            screen: pygame display object.
        """

        # NOTE: Enemy Initializer
        # Initializes the required variables for an enemy.
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.health = health
        self.health_max = health
        self.damage = damage
        self.point_amount = point_amount

        # Initializes the sprite sheet for the respective enemy
        self.sprite_sheet_image = py.image.load(f"sprites{os.sep}{enemy_type}.png").convert_alpha()
        self.sprite_sheet = SpriteSheet(self.sprite_sheet_image)
        self.animation_list = []
        self.animation_steps = [2, 2, 2, 2, 2, 2, 2, 1, 2]
        self.action = 0
        self.frame = 0
        self.last_update = py.time.get_ticks()
        self.enemyBar = HealthBar(0, 0, 0, 0, 'red')

        # Randomizes the enemy spawn point
        rand_pos = rand.randint(1, 4)
        if rand_pos == 1:
            self.y = rand.randint(-150, -50) + display_scroll[1]
            self.x = rand.randint(-150, screen.get_width() + 150) + display_scroll[0]
        if rand_pos == 2:
            self.y = rand.randint(screen.get_height() + 50, screen.get_height() + 150) + display_scroll[1]
            self.x = rand.randint(-150, screen.get_width() + 150) + display_scroll[0]
        if rand_pos == 3:
            self.y = rand.randint(-150, screen.get_height() + 150) + display_scroll[1]
            self.x = rand.randint(-150, -50) + display_scroll[0]
        if rand_pos == 4:
            self.y = rand.randint(-150, screen.get_height() + 150) + display_scroll[1]
            self.x = rand.randint(screen.get_width() + 50, screen.get_width() + 150) + display_scroll[0]

        # Initializes the sprite animation based on the type of enemy.
        if enemy_type == "Monster":
            step_counter = 0
            for animation in self.animation_steps:
                temp_list = []
                for _ in range(animation):
                    temp_list.append(
                        self.sprite_sheet.get_image(step_counter, 8, self.width, self.height, 1, (0, 255, 0)))
                    step_counter += 1
                self.animation_list.append(temp_list)
            self.animation_list[3] = [py.transform.flip(self.animation_list[2][x], True, False) for x in
                                      range(len(self.animation_list[2]))]
        if enemy_type == "Skeleton":
            step_counter = 0
            for animation in self.animation_steps:
                temp_list = []
                for _ in range(animation):
                    temp_list.append(
                        self.sprite_sheet.get_image(step_counter, 8, self.width, self.height, 1, (0, 255, 0)))
                    step_counter += 1
                self.animation_list.append(temp_list)
            self.animation_list[3] = [py.transform.flip(self.animation_list[2][x], True, False) for x in
                                      range(len(self.animation_list[2]))]
        if enemy_type == "Hero":
            step_counter = 0
            for animation in self.animation_steps:
                temp_list = []
                for _ in range(animation):
                    temp_list.append(
                        self.sprite_sheet.get_image(step_counter, 8, self.width, self.height, 1, (0, 255, 0)))
                    step_counter += 1
                self.animation_list.append(temp_list)
            self.animation_list[3] = [py.transform.flip(self.animation_list[2][x], True, False) for x in
                                      range(len(self.animation_list[2]))]
            self.animation_list[5] = [py.transform.flip(self.animation_list[4][x], True, False) for x in
                                      range(len(self.animation_list[4]))]

    def enemy_damage(self, damage) -> bool:
        """
        Damages the enemy based on player damage.
        Parameters:
            damage: damage done by player.
        Returns:
            bool: Whether the enemy is dead based on enemy health.
        """

        # NOTE: Enemy Damaging and Death Section
        # Decreases enemy health and determines the death of the enemy.
        self.health -= damage
        if self.health <= 0:
            return True
        else:
            return False

    def get_enemy_pos(self) -> tuple:
        """
        Returns the enemy position.
        Returns:
            tuple: Enemy current position.
        """

        # NOTE: Enemy Position Return Section
        # Returns the enemy current position.
        return self.x, self.y

    def move(self, unit_vector, player_pos) -> None:
        """
        Moves the enemy based on unit vector (Speed and direction).
        Parameters:
            unit_vector: unit vector to move the enemy (Speed and direction).
            player_pos: position of the player.
        Returns:
            None
        """

        # Moves the enemy and changes the enemy animation direction.
        self.action = get_direction(self.get_enemy_pos(), player_pos)
        self.x, self.y = self.x + unit_vector[0] * self.speed, self.y + unit_vector[1] * self.speed

    def update(self, display, display_scroll) -> None:
        """
        Updates the enemy animation and displays it.
        Parameters:
            display: pygame display object.
            display_scroll: extra position to move the enemy on the screen based on player movement.
        Returns:
            None
        """

        # NOTE: Cycles and Displays Animation Section
        # Updates the enemy animation frame and displays the enemy and health bar.
        current_time = py.time.get_ticks()
        if current_time - self.last_update > self.ANIMATION_COOLDOWN:
            self.frame += 1
            self.last_update = current_time

            if self.frame >= len(self.animation_list[self.action]):
                self.frame = 0
        display.blit(self.animation_list[self.action][self.frame], ((self.x - 64) - display_scroll[0], (self.y - 64) - display_scroll[1]))
        self.enemyBar.update(display, (self.x - display_scroll[0], self.y - display_scroll[1]), self.health, self.health_max)