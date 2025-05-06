### File to create the player ###

import pygame as py
from SpriteSheet import SpriteSheet

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self, display):
        py.draw.rect(display, (0, 0, 0), (self.x - (self.width / 2), self.y - (self.height / 2), self.width, self.height))

class Gun:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self, display):
        pass