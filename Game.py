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
        self.screen = py.display.set_mode(size = (1550, 800), flags = self.flags)
        py.display.set_caption(name)
        self.clock = py.time.Clock()

        self.display_scroll = [0, 0]
        self.counter = 0
        self.bullets = []
        self.enemies = []
        self.player = Player(x = self.screen.get_width() / 2, y = self.screen.get_height() / 2, width = 10, height = 10)
        self.gun = Gun(x = 0, y = 0, width = 50, height = 50)

    def run(self):
        while True:

            for event in py.event.get():
                if event.type == py.QUIT: quit()

            self.screen.fill((0,154,23))

            self.player.update(self.screen)
            py.draw.circle(self.screen, (150, 50, 69), (50 - self.display_scroll[0], 50 - self.display_scroll[1]), 5)

            keys = py.key.get_pressed()
            if keys[py.K_a] and keys[py.K_s]:
                self.display_scroll[0] -= 0.7
                self.display_scroll[1] += 0.7
                self.player.action = 3
            elif keys[py.K_a] and keys[py.K_w]:
                self.display_scroll[0] -= 0.7
                self.display_scroll[1] -= 0.7
                self.player.action = 8
            elif keys[py.K_d] and keys[py.K_s]:
                self.display_scroll[0] += 0.7
                self.display_scroll[1] += 0.7
                self.player.action = 2
            elif keys[py.K_d] and keys[py.K_w]:
                self.display_scroll[0] += 0.7
                self.display_scroll[1] -= 0.7
                self.player.action = 8
            else:
                if keys[py.K_a]:
                    self.display_scroll[0] -= 1
                    self.player.action = 4
                if keys[py.K_d]:
                    self.display_scroll[0] += 1
                    self.player.action = 4
                if keys[py.K_w]:
                    self.display_scroll[1] -= 1
                    self.player.action = 4
                if keys[py.K_s]:
                    self.display_scroll[1] += 1
                    self.player.action = 0

            py.display.flip()

