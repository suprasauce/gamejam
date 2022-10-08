import colors
import pygame as py
import random,math

# class Water:
#   def __init__(self,x,y,height,width) ->None:
#     self.x = x
#     self.y = y
#     self.height = height
#     self.width = width
#     self.surface = py.Surface((width,height))
#   def draw(self,screen,offset):
#     self.surface.fill(colors.DARK_BLUE);
#     screen.blit(self.surface, (self.x+offset, self.y))

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
    #first_sin_input = random.randint(1,90)
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
            offset = py.Vector2((of,0))
            random_width = point[1]//100
            vector_width = py.Vector2(random_width, 0)
            py.draw.line(display, self.high_light_color, point[0]-offset-vector_width, point[0]-offset+vector_width)
  def draw(self,screen,offset):
    self.surface.fill(colors.DARK_BLUE);
    screen.blit(self.surface, (self.position.x+offset, self.position.y))
    self.render(offset,self.surface)
  
    
    
    
