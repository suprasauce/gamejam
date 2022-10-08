import pygame as py
import constants, colors
from player import player

py.init()

screen = py.display.set_mode(constants.SCREEN_SIZE)
clock = py.time.Clock()

run = True
bansal = player(100,100)

while(run):
    clock.tick(constants.FPS)
    screen.fill(colors.WHITE)
    bansal.get_input()
    bansal.move()
    bansal.draw(screen)

    py.display.update()