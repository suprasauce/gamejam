from pickle import FALSE
import pygame as py
import colors, constants, sys

class player:
    def __init__(self, x, y) -> None:
        # x and y are distances w.r.t (0,0)
        self.x = x
        self.y = y
        self.surface = py.Surface(constants.PLAYER_SIZE)
        self.moving_left = False
        self.moving_right = False
        self.jump = True

    def draw(self, screen):
        self.surface.fill(colors.BLACK)
        screen.blit(self.surface, (self.x, self.y))

    def get_input(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            elif event.type == py.KEYDOWN:
                if event.key == py.K_d:
                    self.moving_right = True

                if event.key == py.K_a:
                    self.moving_left = True

                if event.key == py.K_w:
                    self.jump = True

            elif event.type == py.KEYUP:
                if event.key == py.K_d:
                    self.moving_right = False

                if event.key == py.K_a:
                    self.moving_left = False
            #self.move()

    def move(self):
        if self.moving_left:
            self.x -= constants.PLAYER_SPEED
        
        if self.moving_right:
            self.x += constants.PLAYER_SPEED