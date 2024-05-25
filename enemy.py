import pyglet as glet
import setup
from pyglet import sprite
from pyglet.math import Vec2
from player import Player
import math


class Enemy_1(glet.shapes.CenterRectangle):
   """base enemy tybe"""
   _height = setup._screen_height // 15
   _width = setup._screen_height // 15
   _color = (255, 255, 255, 255)
   def __init__(self, 
                map_path:list, 
                player:Player, 
                batch=None, 
                group=None):
      
      self.map_path = map_path
      self.Current_pos = self.map_path[0]
      self.next_pos = 1
      #temp for splitting a to number set : (num , num)
      self.t_x, self.t_y = self.Current_pos
      super().__init__(width=self._width, height=self._height, batch=batch, group=group, x=self.t_x, y=self.t_y, color=self._color)
      self.health = 2
      self.speed = 8
      self.damage = 1
      self.value = 25
      self.has_given_damage = False
      self.has_given_points = False
      self.player = player
   
   def update(self):
      if self.health <= 0:
         self.kill()
      else:
         self.move()
   
   def _Update_x_y(self):
      self.position = self.Current_pos
      self._path_rotate()

   def take_damage(self, damage: float):
      print("toke damage")
      self.healt -= damage

   def move(self):
      if self.next_pos < len(self.map_path):
         self.target = self.map_path[self.next_pos]
         self.movement = self.target - self.Current_pos

          # calc distance from target
         distance = self.Current_pos.distance(self.target)
         if distance >= self.speed : 
            self.Current_pos += self.movement.normalize() * self.speed
         else:
            self.Current_pos += self.movement.normalize() * distance
         
         # sets new target if target reached
         if distance == 0.0 : 
            self.next_pos += 1

         self._Update_x_y()

      else: # End reached
         self.give_damage()
      
   def give_damage(self):
      if self.has_given_damage == False:
            self.player.player_take_damge(self.damage)
            self.has_given_damage = True
            
      if self.has_given_damage == True:
         self.delete()

   def _path_rotate(self):
      #calc rotation
      distance = self.target - self.Current_pos
      self.angle = math.degrees( math.atan2(distance[0], distance[1]))
      self.rotation = self.angle

   def take_damage(self, damege:int):
      self.health -= damege
         
   
   def kill(self):
      if self.has_given_points == False:
         self.player.player_give_points(points=self.value)
         self.has_given_points = True
      else:
         self.delete()

class Enemy_2(Enemy_1):
   """fast and nimble"""
   _height = setup._screen_height // 30
   _width = setup._screen_height // 30
   _color = (60, 60, 60, 255)
   def __init__(self, 
                map_path:list, 
                player:Player, 
                batch=None, 
                group=None):
      #temp for splitting a to number set : (num , num)
      super().__init__(map_path = map_path, 
                player = player, 
                batch=batch, 
                group=group)
      self.healt = 1
      self.speed = 6
      self.damage = 3
      self.value = 35
   
class Enemy_3(Enemy_1):
   """slow and strong"""
   _height = setup._screen_height // 12
   _width = setup._screen_height // 12
   _color = (130, 200, 150, 255)
   def __init__(self, 
                map_path:list, 
                player:Player, 
                batch=None, 
                group=None):
      #temp for splitting a to number set : (num , num)
      super().__init__(map_path = map_path, 
                player = player, 
                batch=batch, 
                group=group)
      self.healt = 50
      self.speed = 0.5
      self.damage =25
      self.value = 50


class Enemy_group():
   def __init__(self, densetey:float = 1):
      """containes a list of enemy obj's, use this for ease of controling multiable enemys
      enemy_densetey scale enemy staggaring use [0.5 -> 6] to leave dicent space between enemys"""
      self.enemy_list = []
      self.deley = 0.0
      self.enemy_densetey = 0.01 * densetey # set spaceing
   
   def add(self, value:Enemy_1):
      """adds one enemy to the group"""
      self.enemy_list.append

   def replace(self, value:list[Enemy_1]):
      """replaces the whole list, with value"""
      self.enemy_list = value
   
   @property   
   def number_of_enemys(self) -> int:
      return len(self.enemy_list)
     
   def Auto_Fill_list(self, 
                      number_of_enemys:int,
                      map:list,
                      player:Player,
                      gr_group:glet.graphics.Group,
                      gr_batch:glet.graphics.Batch):
      points = number_of_enemys * 100 ** 1.05
      temp = []
      for num in range(0, number_of_enemys):
         if points >= 1000:
            temp.append(Enemy_3(map_path=map,
                                 player=player,
                                 group=gr_group,
                                 batch=gr_batch))
            points -= 800
         if points >= 500:
            temp.append(Enemy_2(map_path=map,
                                 player=player,
                                 group=gr_group,
                                 batch=gr_batch))
            points -= 450
         if points >= 100:
            temp.append(Enemy_1(map_path=map,
                                 player=player,
                                 group=gr_group,
                                 batch=gr_batch))
            points -= 70
      self.enemy_list = temp[::-1]

   def SendOut(self):
      if len(self.enemy_list) < 1: 
         raise Exception(f"missing enemy in list. \n{self.enemy_list}", )
      
      for i, e in zip(range(1, self.number_of_enemys + 1), self.enemy_list):
         if math.floor(self.deley) > i: 
            e.update()
      self.deley += self.enemy_densetey
