### File to create the player ###

import pygame as py
from SpriteSheet import SpriteSheet
import os

class Player:
    ANIMATION_COOLDOWN = 175
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprite_sheet_image = py.image.load(f"sprites{os.sep}base_character.png").convert_alpha()
        self.sprite_sheet = SpriteSheet(self.sprite_sheet_image)
        self.animation_list = []
        self.animation_steps = [2, 2, 2, 2, 2, 2, 2, 1, 2]
        # 0 or 1 = s, 2 = s+d, 4 or 5 or 6 = a or d or w, 8 = w+d or w+a, 3 = s+a
        self.action = 2
        self.last_update = py.time.get_ticks()
        self.frame = 0
        step_counter = 0
        for animation in self.animation_steps:
            temp_list = []
            for _ in range(animation):
                temp_list.append(self.sprite_sheet.get_image(step_counter, 8, 128, 128, 1, (0, 255, 0)))
                step_counter += 1
            self.animation_list.append(temp_list)
        self.animation_list[3] = [py.transform.flip(self.animation_list[2][x], True, False) for x in range(len(self.animation_list[2]))]

    def update(self, display):

        current_time = py.time.get_ticks()
        if current_time - self.last_update > self.ANIMATION_COOLDOWN:
            self.frame += 1
            self.last_update = current_time

            if self.frame >= len(self.animation_list[self.action]):
                self.frame = 0
        display.blit(self.animation_list[self.action][self.frame], (self.x - 64, self.y - 64))


class Gun:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self, display):
        pass