from random import random
import pygame as py
import random, constants, colors

class plat:
    def __init__(self, prev_x) -> None:
            self.x =  constants.PLATFORM_SEPRATION + prev_x
            self.y = constants.SCREEN_HEIGHT/2.0 + random.choice([0,10,20,50])
            self.width = constants.PLATFORM_WIDTH + random.choice([-10,20,60])
            self.height = constants.SCREEN_HEIGHT - self.y
            self.surface = py.Surface((self.width, self.height))

    def draw(self, screen, offset):
        self.surface.fill(colors.BLACK)
        screen.blit(self.surface, (self.x + offset, self.y))