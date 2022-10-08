import colors
import pygame as py

class Fire:
  def __init__(self,x,y,height,width) ->None:
    self.x = x
    self.y = y
    self.height = height
    self.width = width
    self.surface = py.Surface((width,height))
  def draw(self,screen,offset):
    self.surface.fill(colors.LIGHT_RED);
    screen.blit(self.surface, (self.x+offset, self.y))
    
    
