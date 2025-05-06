### File to create the enemies ###

import pygame as py
from SpriteSheet import SpriteSheet

class Enemy:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self, display):
        pass