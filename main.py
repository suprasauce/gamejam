import pygame as py
import constants, colors

py.init()

screen = py.display.set_mode(constants.SCREEN_SIZE)
clock = py.time.Clock()

run = True

while(run):
    clock.tick(constants.FPS)
    screen.fill(colors.WHITE)

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    py.display.update()