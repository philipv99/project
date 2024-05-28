import pyglet as glet
import setup
import tower
from pyglet.math import Vec2

_game_difficulty_player_stats = [
   #hp,  gold, start round
   [100, 1000,  0],
   [ 50,  650,  1],
   [  1,  500,  2]
]

class Player:
   """
   game instens of GUI, hp and points. 
   player controls game_difficulty
   """
   def __init__(self, group:glet.graphics.Group, gameover_batch:glet.graphics.Batch, batch:glet.graphics.Batch ,gameover_group:glet.graphics.Group, game_difficulty: int = 1 or 2 or 3, ):
      self._text_Life = " / Life"
      self._text_points = " / Points"
      self._text_round = "Round: "
      self._text_enemys = "Enemys in round: "
      self.enemys_in_round = 0
      self.difficulty = game_difficulty
      self._hp = _game_difficulty_player_stats[self.difficulty][0]
      self._gold = _game_difficulty_player_stats[self.difficulty][1]
      self._Round = _game_difficulty_player_stats[self.difficulty][2]
      self.player_towers = []
      self.player_group = group
      self.player_batch = batch
      self.loost_game = False

      self.gameover_group = gameover_group
      self.gameover_batch = gameover_batch

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
      
      self.Round_label = glet.text.Label(f"{self._text_round}{self._Round}", 
                       x= setup._UI_margin, 
                       y= setup._screen_height - setup._UI_margin_y, 
                       font_name=setup._font_famalie,
                       bold=True, 
                       font_size= setup._font_size_header,
                       color=(255, 255, 255, 255),
                       group=self.player_group,
                       batch=self.player_batch)
      
      self.enemy_label = glet.text.Label(f"{self._text_round}{self._Round}", 
                       x= setup._UI_margin, 
                       y= setup._screen_height - setup._UI_margin_y - 20, 
                       font_name=setup._font_famalie,
                       bold=False, 
                       font_size= setup._font_size_text,
                       color=(255, 255, 255, 255),
                       group=self.player_group,
                       batch=self.player_batch)
      
      self.game_over_label = glet.text.Label(f"GAME OVER", 
                       x= (setup._screen_width + setup._game_side_pannel) // 2, 
                       y= setup._screen_height // 2 + 10, 
                       font_name=setup._font_famalie,
                       bold = True, 
                       anchor_x="center", 
                       anchor_y="center", 
                       font_size= setup._font_size_header + 30,
                       color=(255, 20, 20, 255),
                       batch=self.gameover_batch,
                       group=self.gameover_group)
      
      self.game_over_under_label = glet.text.Label(f"You made it {self._Round} rounds!", 
                       x= (setup._screen_width + setup._game_side_pannel) // 2, 
                       y= setup._screen_height // 2 - 40, 
                       font_name=setup._font_famalie,
                       bold = False, 
                       anchor_x="center", 
                       anchor_y="center", 
                       font_size= setup._font_size_mid + 10,
                       color=(255, 20, 20, 255),
                       batch=self.gameover_batch,
                       group=self.gameover_group)
      
      self.trans_bg = glet.shapes.Rectangle(
         x = 0, 
         y = 0,
         width = setup._screen_width + setup._game_side_pannel,
         height= setup._screen_height,
         color =(0,0,0,180),
         batch = self.gameover_batch,
         group = self.gameover_group 
      )
      
      
   def draw(self):
      self.player_batch.draw()

   def player_take_damge(self, damage: int):
      self._hp -= damage
      self.Life_label.text = str(self._hp) + self._text_Life
      if self._hp <= 0: 
         self.loost_game = True
         self.gameover_group.visible = True

   def player_take_points(self, points: int):
      """take points from player"""
      self._gold -= points
      self.Gold_label.text = str(self._gold) + self._text_points

   def player_give_points(self, points: int):
      """give points to player"""
      self._gold += points
      self.Gold_label.text = str(self._gold) + self._text_points
      
   def increase_round(self, round):
      self._Round = round
      self.Round_label.text = self._text_round + str(self._Round)
      self.game_over_under_label.text = f"You made it {self._Round} rounds!"

   def number_of_enemys_in_rounds(self, number:int):
      self.enemys_in_round = number
      self.enemy_label.text = self._text_enemys + str(self.enemys_in_round)

   def add_tower(self, tower, map:list):
      # can afford tower
      if self._gold < tower.cost:
         raise Exception("cant afford tower")
               
      # dicdence to other towers
      for t in self.player_towers:
         tx = range(t._x - (t.width // 2), t._x + (t.width // 2))
         ty = range(t._y - (t.height // 2), t._y + (t.height // 2))
         if tower._x in tx and tower._y in ty:
            raise Exception("to cloce to other tower")
      self.player_take_points(tower.cost)
      self.player_towers.append(tower)

   def Tower_update(self, enemy_list:list):
      for T in self.player_towers:
         T.update(enemy_list)