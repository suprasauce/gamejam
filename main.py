import sys
import pygame as py
import constants, colors
from player import player
from plat import plat

py.init()

screen = py.display.set_mode(constants.SCREEN_SIZE)
clock = py.time.Clock()

run = True
bansal = player(constants.SCREEN_WIDTH/2.0,100)
scroll = 0
offset = 0
platforms = [plat(constants.SCREEN_WIDTH/2.0 - constants.PLATFORM_SEPRATION - bansal.width/2.0)]

while(run):
    clock.tick(constants.FPS)
    screen.fill(colors.WHITE)

    #print(len(platforms))
    while platforms[-1].x + platforms[-1].width + offset <= constants.SCREEN_WIDTH:
        next_platform = plat(platforms[-1].x + platforms[-1].width)
        platforms.append(next_platform)
    
    for platform in platforms:
        platform.draw(screen, offset)

    bansal.get_input()
    scroll, offset = bansal.move(platforms, offset)
    bansal.draw(screen)

    # to be removed
    if bansal.y > constants.SCREEN_HEIGHT:
        py.quit()
        sys.exit()

    py.display.update()