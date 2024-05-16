import pyglet as glet
import setup

_game_difficulty_player_stats = [
   #hp,  gold, start round
   [100, 1000,  0],
   [ 50,  650,  0],
   [  1,  500,  0]
]

class Player:
   """
   game instens of GUI, hp and points. 
   player controls game_difficulty
   """
   def __init__(self, group:glet.graphics.Group, batch:glet.graphics.Batch, game_difficulty: int = 1 or 2 or 3, ):
      self._text_Life = " / Life"
      self._text_points = " / Points"
      self.difficulty = game_difficulty
      self._hp = _game_difficulty_player_stats[self.difficulty][0]
      self._gold = _game_difficulty_player_stats[self.difficulty][1]
      self._Round = _game_difficulty_player_stats[self.difficulty][2]

      self.player_group = group
      self.player_batch = batch

      self.Life_label = glet.text.Label(f"{self._hp}{self._text_Life}", 
                       x= setup._screen_width - setup._UI_margin, 
                       y= setup._screen_height - setup._UI_margin_y, 
                       anchor_x="right", 
                       font_name=setup._font_famalie,
                       bold=True, 
                       font_size= setup._font_size_header,
                       color=(230, 70, 70, 255),
                       group=self.player_group,
                       batch=self.player_batch)
      
      self.Gold_label = glet.text.Label(f"{self._gold}{self._text_points}", 
                       x= setup._screen_width - setup._UI_margin, 
                       y= setup._screen_height - setup._UI_margin_y - 30, 
                       anchor_x="right", 
                       font_name=setup._font_famalie,
                       bold=True, 
                       font_size= setup._font_size_header,
                       color=(200, 150, 50, 255),
                       group=self.player_group,
                       batch=self.player_batch)  
      
   def draw(self):
      self.player_batch.draw()

   def player_take_damge(self, damage: int):
      if damage > 0 :
         self._hp -= damage
         self.Life_label.text = str(self._hp) + self._text_Life

   def player_take_points(self, points: int):
      """take points from player"""
      self.gold -= points
      self.Gold_label.text += str(self._gold) + self._gold_Life

   def player_give_points(self, points: int):
      """give points to player"""
      self.gold += points
      self.Gold_label.text += str(self._gold) + self._gold_Life
      