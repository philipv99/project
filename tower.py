import pyglet as glet
import math


image_tower_1 = glet.image.load('assets/img/turret_1.png')
image_tower_1.anchor_x = image_tower_1.width // 2
image_tower_1.anchor_y = image_tower_1.height // 2


class turret_1(glet.sprite.Sprite):
   def __init__(self, x, y, batch=None, group=None, group_gui=None):
      self.cost = 100
      self.range = 200
      self.cool_down = 2
      self.current_cool_down_time = 5.0
      self.damage = 1
      self.target = None
      super(turret_1, self).__init__(img = image_tower_1, x = x, y = y, batch=batch, group=group)
      self.anchor_x = 'center'
      self.anchor_y = 'center'
      self.radius = glet.shapes.Circle(x=x, y=y, radius=self.range, color=[255, 0, 0, 40], batch=batch, group=group_gui)

   def draw(self):
      self.draw()
      self.radius.draw()

   def update(self, dt, enemy_list):
      if self.current_cool_down_time < self.cool_down:
         self.current_cool_down_time += dt
      self.pick_target(enemy_list)
      if self.target is not None and self.current_cool_down_time >= self.cool_down:
         self.shoot_target()
      else:
         print(self.target , "True" if self.current_cool_down_time >= 2 else "False")
         

   def pick_target(self, enemy_list):
      # find target to shoot
      x_desince = 0
      y_desince = 0
      # distence for each enemy 
      for enemy in enemy_list: 
         x_desince = enemy._x - self._x
         y_desince = enemy._y - self._y
         dist = math.sqrt(x_desince ** 2 + y_desince ** 2)
         if self.range < dist:
            self.target = None
         else:
            self.rotation = math.degrees(math.atan2(x_desince, y_desince))
            self.target = enemy
            break

   def shoot_target(self):
      self.target.take_damage(self.damage)
      print("shot enemy")
      # resets turret
      self.current_cool_down_time = 0
      self.target = None
