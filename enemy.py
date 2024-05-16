import pyglet as glet
import setup
from pyglet import sprite
from pyglet.math import Vec2
from player import Player
import math

class Enemy(glet.shapes.CenterRectangle):
   _height = setup._screen_height // 15
   _width = setup._screen_height // 15
   _color = (255, 255, 255, 255)
   def __init__(self, 
                map_path:list, 
                player:Player, batch=None, 
                group=None, healt:float=20, 
                speed:float=2, 
                damage:int=1):
      
      self.map_path = map_path
      self.Current_pos = self.map_path[0]
      self.next_pos = 1
      #temp for splitting a to number set : (num , num)
      self.t_x, self.t_y = self.Current_pos
      super().__init__(width=self._width, height=self._height, batch=batch, group=group, x=self.t_x, y=self.t_y)
      self.healt = healt
      self.speed = speed
      self.damage = damage
      self.has_given_damage = False
      self.player = player
   
   
   def _Update_x_y(self):
      self.position = self.Current_pos
      self._path_rotate()

   def take_damage(self, damage: float):
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

     
