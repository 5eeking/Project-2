### File to create the enemies ###
# TODO: ADD DOCSTRINGS AND COMMENTS.

# NOTE: Import Section
# Imports required modules for the file
import pygame as py
from Logic import *
from SpriteSheet import SpriteSheet
from HealthBar import HealthBar
import random as rand
import os

class Enemy:
    ANIMATION_COOLDOWN = 175
    def __init__(self, x, y, speed, width, height, enemy_type, health, damage, point_amount, display_scroll, screen) -> None:

        # NOTE: Enemy Initializer
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.health = health
        self.health_max = health
        self.damage = damage
        self.point_amount = point_amount

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

    # Decreases the health of the enemy and returns whether it's dead or not
    def enemy_damage(self, damage) -> bool:

        # NOTE: Enemy Damaging and Death Section
        self.health -= damage
        if self.health <= 0:
            return True
        else:
            return False

    # Returns the enemy position
    def get_enemy_pos(self) -> tuple:

        # NOTE: Enemy Position Return Section
        return self.x, self.y

    def move(self, unit_vector, player_pos) -> None:
        self.action = get_direction(self.get_enemy_pos(), player_pos)
        self.x, self.y = self.x + unit_vector[0] * self.speed, self.y + unit_vector[1] * self.speed

    def update(self, display, display_scroll) -> None:

        # NOTE: Cycles and Displays Animation Section
        current_time = py.time.get_ticks()
        if current_time - self.last_update > self.ANIMATION_COOLDOWN:
            self.frame += 1
            self.last_update = current_time

            if self.frame >= len(self.animation_list[self.action]):
                self.frame = 0
        display.blit(self.animation_list[self.action][self.frame], ((self.x - 64) - display_scroll[0], (self.y - 64) - display_scroll[1]))
        self.enemyBar.update(display, (self.x - display_scroll[0], self.y - display_scroll[1]), self.health, self.health_max)