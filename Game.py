### File that runs the game and connects all required files ###

from Player import *
import pygame as py
import math
import random as rand
import numpy as np

class Game:
    def __init__(self, name):

        py.init()
        self.flags = py.RESIZABLE | py.SCALED
        self.screen = py.display.set_mode(size = (500, 500), flags = self.flags)
        py.display.set_caption(name)
        self.clock = py.time.Clock()

        self.counter = 0
        self.bullets = []
        self.enemies = []
        self.player = Player(x = self.screen.get_width() / 2, y = self.screen.get_height() / 2, width = 50, height = 50)
        self.gun = Gun(0, 0, 50, 50)

    def run(self):
        while True:

            for event in py.event.get():
                if event.type == py.QUIT: quit()

            self.screen.fill((255, 255, 255))

            self.player.update(self.screen)

            py.display.flip()

