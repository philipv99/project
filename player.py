import pyglet as glet
import setup

class Player:
   def __init__(self, game_difficulty: int = 1 or 2 or 3):
      if game_difficulty == 1:
         self._hp = 100
         self._gold = 1000
         self._Round = 0
      if game_difficulty == 2:
         self._hp = 100
         self._gold = 650
         self._Round = 0
      if game_difficulty == 3:
         self._hp = 1
         self._gold = 650
         self._Round = 0

      self.player_batch = glet.graphics.Batch()

      self.Life_label = glet.text.Label(f"{self._hp} / Lifes", 
                       x= setup._screen_width - setup._UI_margin, 
                       y= setup._screen_height - setup._UI_margin_y, 
                       anchor_x="right", 
                       font_name=setup._font_famalie,
                       bold=True, 
                       font_size= setup._font_size_header,
                       color=(230, 70, 70, 255),
                       batch=self.player_batch)
      
      self.Gold_label = glet.text.Label(f"{self._gold} / Gold", 
                       x= setup._screen_width - setup._UI_margin, 
                       y= setup._screen_height - setup._UI_margin_y - 30, 
                       anchor_x="right", 
                       font_name=setup._font_famalie,
                       bold=True, 
                       font_size= setup._font_size_header,
                       color=(200, 150, 50, 255),
                       batch=self.player_batch)  
      
   def draw(self):
      self.player_batch.draw()
      