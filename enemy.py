import random
import pyglet as glet
import setup
from pyglet import sprite
from pyglet.math import Vec2
from player import Player
import math

#! ------------------------------------ enemy ----------------------------------- #
class Enemy_1(glet.shapes.CenterRectangle):
   """base enemy tybe"""
   _height = setup._screen_height // 15
   _width = setup._screen_height // 15
   _color = (255, 255, 255, 255)
   _health = 2
   _speed = 3
   _damage = 1
   _value = 5
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
      self.health =  self._health
      self.speed  =  self._speed
      self.damage =  self._damage
      self.value  =  self._value
      self.has_given_damage = False
      self.has_given_points = False
      self.moveing = False
      self.player = player
   
   def update(self, dt):
      if self.Current_pos == self.map_path[-1]: # End reached
         self.give_damage()
      else:
         self.move()
         
   
   def _Update_x_y(self):
      self.position = self.Current_pos
      self._path_rotate()

   def take_damage(self, damage: float):
      self.healt -= damage

   def move(self):
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
      try:
            self._Update_x_y()
      except Exception as err:
         print(err)
     
   def move_schedule(self, dt):
      self.moveing == True
      glet.clock.schedule_interval_soft(self.update, 1/60)

   
   def give_damage(self):
      if self.has_given_damage == False:
         self.player.player_take_damge(self.damage)
         self.has_given_damage = True     
      

   def _path_rotate(self):
      #calc rotation
      distance = self.target - self.Current_pos
      self.angle = math.degrees( math.atan2(distance[0], distance[1]))
      self.rotation = self.angle


   def kill(self):
      glet.clock.unschedule(self.update)
      self.delete()



#! ------------------------------------ enemy ----------------------------------- #
class Enemy_2(Enemy_1):
   """fast and nimble"""
   _height = setup._screen_height // 30
   _width = setup._screen_height // 30
   _color = (60, 60, 60, 255)
   _health = 3
   _speed = 6
   _damage = 1
   _value = 10
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

#! ------------------------------------ enemy ----------------------------------- #  
class Enemy_3(Enemy_1):
   """slow and strong"""
   _height = setup._screen_height // 12
   _width = setup._screen_height // 12
   _color = (130, 200, 150, 255)
   _health = 50
   _speed = 0.5
   _damage = 25
   _value = 25
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

#* ------------------------------------ group ----------------------------------- #
class Enemy_group():
   def __init__(self, player:Player, round:int, map:list, gr_group:glet.graphics.Group,
                                                          gr_batch:glet.graphics.Batch):
      """containes a list of enemy obj's, use this for ease of controling multiable enemys
      enemy_densetey scale enemy staggaring use [0.5 -> 6] to leave dicent space between enemys"""
      self.enemy_list = []
      self.deley = 0.0
      self.enemy_densetey = 0.01 * 2 # set spaceing
      self.current_round = round
      self.map = map
      self.player = player
      self.gr_group = gr_group
      self.gr_batch = gr_batch
   
   def add(self, value:Enemy_1):
      """adds one enemy to the group"""
      self.enemy_list.append(value)

   def replace(self, value:list[Enemy_1]):
      """replaces the whole list, with value"""
      self.enemy_list = value
   
   @property   
   def number_of_enemys(self) -> int:
      return len(self.enemy_list)
     
   def Create_round(self):
      points = 200 + (50*self.current_round) + self.current_round ** 2
      temp = []
      while points > 49:
         if points >= 800:
            temp.append(Enemy_3(map_path=self.map,
                                 player=self.player,
                                 group=self.gr_group,
                                 batch=self.gr_batch))
            points -= 800
         if points >= 300:
            temp.append(Enemy_2(map_path=self.map,
                                 player=self.player,
                                 group=self.gr_group,
                                 batch=self.gr_batch))
            points -= 300
         if points >= 50:
            temp.append(Enemy_1(map_path=self.map,
                                 player=self.player,
                                 group=self.gr_group,
                                 batch=self.gr_batch))
            points -= 50
      self.enemy_list = temp[::-1]
      self.player.number_of_enemys_in_rounds(len(self.enemy_list))

   def update(self):
      if len(self.enemy_list) == 0:
         self.current_round += 1
         self.player.increase_round(self.current_round)
         self.player.player_give_points(math.floor(100 + self.current_round ** 1.2))
         self.Create_round()

      else:
         self.SendOut()

   def SendOut(self):
      for enemy, num in zip(self.enemy_list, range(0, len(self.enemy_list))):
         if enemy.has_given_damage == True:
            self.enemy_list.remove(enemy)
            enemy.kill()
         else:
            if enemy.moveing == False:
               glet.clock.schedule_once(enemy.move_schedule, num * (0.8 + random.random()))
               enemy.moveing = True

   def shoot_target_enemy(self, enemy, damge:int):
      if enemy.health - damge < 1:
         enemy.player.player_give_points(points=enemy.value)
         self.enemy_list.remove(enemy)
         enemy.kill()
      else:
         enemy.health -= damge