import pyglet as glet
import math


image_tower_1 = glet.image.load('assets/img/turret_1.png')
image_tower_1.anchor_x = image_tower_1.width // 2
image_tower_1.anchor_y = image_tower_1.height // 2

image_tower_2 = glet.image.load('assets/img/turret_2.png')
image_tower_2.anchor_x = image_tower_2.width // 2
image_tower_2.anchor_y = image_tower_2.height // 2


class turret_1(glet.sprite.Sprite):
   _image_tower = image_tower_1
   _cost      = 100
   _range     = 200
   _cool_down = 2
   _damage    = 1
   def __init__(self, x, y, batch=None, group=None, group_gui=None):
      self.cost      = self._cost 
      self.range     = self._range
      self.cool_down = self._cool_down
      self.damage    = self._damage
      self.ready     = True
      self.target    = None
      super(turret_1, self).__init__(img = self._image_tower, x = x, y = y, batch=batch, group=group)
      self.anchor_x = 'center'
      self.anchor_y = 'center'
      self.radius = glet.shapes.Circle(x=x, y=y, radius=self.range, color=[255, 0, 0, 40], batch=batch, group=group_gui)

   def draw(self):
      self.draw()
      self.radius.draw()

   def update(self, enemy_group):
      self.pick_target(enemy_group.enemy_list)
      if self.target is not None and self.ready is True:
         self.shoot_target(enemy_group)

         

   def pick_target(self, enemy_list):
      x_desince = 0
      y_desince = 0
      # distence for each enemy 
      for enemy in enemy_list: 
         x_desince = enemy._x - self._x
         y_desince = enemy._y - self._y
         # if enemy is in range 200 set as target
         dist = math.sqrt(x_desince ** 2 + y_desince ** 2)
         if self.range < dist:
            glet.clock.schedule_once( self.target_none, 1/60 )
         else: # find target to shoot
            self.rotation = math.degrees(math.atan2(x_desince, y_desince))
            self.target = enemy
            break

   def shoot_target(self, enemy_group):
      enemy_group.shoot_target_enemy(self.target , self.damage)
      self.target = None
      self.ready = False
      glet.clock.schedule_once( self.target_none, 1/10 )
      glet.clock.schedule_once( self.turret_ready, self.cool_down )

   def target_none(self, dt):
      self.target = None

   def turret_ready(self, dt):
      self.ready = True


class turret_2(turret_1):
   _image_tower = image_tower_2
   _cost      = 400
   _range     = 400
   _cool_down = 5
   _damage    = 10
   def __init__(self, x, y, batch=None, group=None, group_gui=None):
      super().__init__(x = x, y = y, batch=batch, group=group, group_gui=group_gui)