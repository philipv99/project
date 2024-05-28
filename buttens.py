import pyglet as glet
import setup


t1_butten = glet.image.load("assets/bottens/t1.png")
t1_pressed = glet.image.load("assets/bottens/t1_pressed.png")
t3_butten = glet.image.load("assets/bottens/t3.png")

speed = glet.image.load("assets/bottens/speed.png")
speed2 = glet.image.load("assets/bottens/speed_pressed.png")


class turret_button(glet.gui.PushButton):
   def __init__(self, x= setup._screen_width  + (setup._game_side_pannel // 6 ) * 1,
                      y=(setup._screen_height // 12) * 10, 
                      group = None, batch = None):
      super().__init__( x = x, y = y,
                     depressed= t1_butten,
                     pressed= t1_pressed,
                     batch= batch,
                     group= group)
      self.toggle = False
   
   def on_press(self):
      if self.toggle:
         self.toggle = False
         self.value = False
      else:
         self.toggle = True
         self._pressed = True

   def place_tower(self, x:int, y:int):
      if x > setup._screen_width:
         return False
      else:
         return True
      

class Speed_button(glet.gui.PushButton):
   def __init__(self, func, group = None, batch = None):
      super().__init__( x= setup._screen_width  + (setup._game_side_pannel // 6 ) * 1 , 
                        y=(setup._screen_height // 12) * 1,
                     depressed= speed,
                     pressed= speed2,
                     batch= batch,
                     group= group)
      self.toggle_speed = False
      self.func = func
   
   def on_press(self):
      if self.toggle_speed == True:
         self.toggle_speed = False
         self.func(self.toggle_speed)
      else:
         self.toggle_speed = True
         self.func(self.toggle_speed)
         self.value = False
      print("speed:", self.toggle_speed)

      