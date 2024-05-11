import pyglet as glet
from pyglet import shapes

class Tank():
   _width = 120
   _height = 120
   _color = [100, 200, 120] # green
   _color_barrel = [160, 250, 160] # ligther green
   _color_barrel_house = [140, 240, 140] # ligther green
   _classBatch = glet.graphics.Batch()
   def __init__(self, x: int, y: int, range: int=200):
      """ Home made tank object, uses shapes to make a tank,
      - draw(), to draw the the object in its own batch
      - rotate(dec: int) head of the thank, dec: degrease. 
         -2 <= dec >= 2
      """
      self.range = range
      self.x = x
      self.y = y
      # shapes
      self.radius = glet.shapes.Circle(x=self.x, y=self.y, radius=self.range, color=[255, 0, 0, 50], batch=self._classBatch)
      self.body = glet.shapes.CenterRectangle(x=self.x, y=self.y, width=self._width, height=self._height, color=self._color, batch=self._classBatch)
      self.tred_left = glet.shapes.CenterRectangle(x=self.x - (self._width // 2), y=self.y, width=self._width // 4, height=self._height + 20, color=[50, 50, 50], batch=self._classBatch)
      self.tred_right = glet.shapes.CenterRectangle(x=self.x + (self._width // 2), y=self.y, width=self._width // 4, height=self._height + 20, color=[50, 50, 50], batch=self._classBatch)
      self.barral = glet.shapes.Line(x=self.x, y=self.y, x2=self.x , y2=self.y+(self._height // 2 + 30), width=18, color=self._color_barrel, batch=self._classBatch)
      self.body_house = glet.shapes.CenterRectangle(x=self.x, y=self.y, width=self._width // 2, height=self._height // 2, color=self._color_barrel_house, batch=self._classBatch)     
      
   def draw(self):
      self._classBatch.draw()

   def update(self):
      self.radius.update()
      self.barral.update()

   def rotate(self, dec: int):
      if dec > 2 : 
         dec = 2
      if dec < -2:
         dec = -2
      self.barral.rotation += dec
      self.body_house.rotation += dec
