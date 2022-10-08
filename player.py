from pickle import FALSE
from turtle import left
import pygame as py
import colors, constants, sys,time

class player:
    def __init__(self, x, y) -> None:
        # x and y are distances w.r.t (0,0)
        self.x = x
        self.y = y
        self.left_leg_x = self.x
        self.right_leg_x = self.x+35
        self.left_leg_y = self.y+50
        self.right_leg_y = self.y+50
        self.left_leg_deg = 0;
        self.right_leg_deg = 0;
        self.surface = py.Surface(constants.PLAYER_SIZE)
        self.left_leg = py.Surface(constants.LEG_SIZE,py.SRCALPHA)
        self.right_leg = py.Surface(constants.LEG_SIZE,py.SRCALPHA)
        self.moving_left = False
        self.moving_right = False
        self.jump = True

    def draw(self, screen):
        self.surface.fill(colors.BLACK)
        self.left_leg.fill(colors.BLACK)
        self.right_leg.fill(colors.BLACK)
        screen.blit(self.surface, (self.x, self.y))
        screen.blit(py.transform.rotate(self.left_leg,self.left_leg_deg), (self.left_leg_x, self.left_leg_y))
        screen.blit(py.transform.rotate(self.right_leg,self.right_leg_deg), (self.right_leg_x, self.right_leg_y))

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

    def move(self,screen):
        if self.moving_left:
            self.x -= constants.PLAYER_SPEED
            # while(self.moving_left)
            if(self.left_leg_deg  >= 30):
                self.left_leg_deg -= 5
            if(self.left_leg_deg  <= 0):
                self.left_leg_deg += 5
            self.left_leg_x -= constants.PLAYER_SPEED
            self.right_leg_x -= constants.PLAYER_SPEED
        else:
            self.left_leg_deg = 0;
        
        
        if self.moving_right:
            self.x += constants.PLAYER_SPEED

            if(self.right_leg_deg  <= 0):
                self.right_leg_deg += 5
            if(self.right_leg_deg  >= 30):
                self.right_leg_deg -= 5

            self.left_leg_x += constants.PLAYER_SPEED
            self.right_leg_x += constants.PLAYER_SPEED
        else:
            self.right_leg_deg = 0

            