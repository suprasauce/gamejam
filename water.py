from asyncio import constants
import colors,constants
import pygame as py
import random,math

class Water:
  def __init__(self, x,y,height,width) -> None:
    self.position = py.Vector2((x,y))
    self.height = height
    self.width = width
    self.base_water_color = '#3D897B'
    self.high_light_color = '#6DBDAF'
    self.surface = py.Surface((width,height))
    self.points = []
    self.populate()
  def populate(self):
    random.seed(None)

    for i in range(6):
        point_xy = py.Vector2(self.position.x+random.randint(2, 32)+i*random.randint(6, 9), self.position.y+random.randint(12, 52))
        self.points.append([point_xy, random.randint(1,359)])

  def wave(self, point: py.Vector2, sin_input: int):
        speed = random.randint(1,2)
        sin_input += speed
        if sin_input >= 360:
            sin_input = 0
        point.y += (math.sin(math.radians(sin_input)))/random.randint(20,25)
        return sin_input

  def update(self):
    for point in self.points:
        point[1] = self.wave(point[0], point[1])

  def render(self, of, display):
    for point in self.points:
        random_width = point[1]//20
        vector_width = py.Vector2(random_width, 0)
        for i in range(1,7,2):
          offset = py.Vector2((of+i*constants.PLATFORM_SEPRATION/7,0))
          py.draw.line(display, self.high_light_color, point[0]+offset-vector_width, point[0]+offset+vector_width)
          
  def draw(self,screen,offset):
    self.surface.fill(colors.DARK_BLUE);
    screen.blit(self.surface, (self.position.x+offset, self.position.y))
    self.render(offset,screen)
  
    
    
    
