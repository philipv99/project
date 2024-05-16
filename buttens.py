import pyglet as glet
import setup


t1_butten = glet.image.load("assets/bottens/t1.png")
t2_butten = glet.image.load("assets/bottens/t2.png")
t3_butten = glet.image.load("assets/bottens/t3.png")


class myButton(glet.gui.PushButton):
   def __init__(self, group = None, batch = None):
      super().__init__(x=setup._screen_width + (setup._game_side_pannel // 3 - 30), 
                     y=setup._screen_height - (t1_butten.height * 1.1),
                     depressed= t1_butten,
                     pressed= t1_butten,
                     batch= batch,
                     group= group)
      self.toggle = False
      
   def on_press(self):
      self.toggle = self.toggle
      print(f"t1 pressed, {self.toggle}")

   def on_release(self):
      print("t1 depressed")
      