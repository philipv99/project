#pyglet
import pyglet as glet
# my own
from buttens import myButton
from tower import *
import setup
import maps
from player import Player
import enemy


# laver  vinduer til at havde spillet i.
window = glet.window.Window(width=setup._screen_width + setup._game_side_pannel, 
                            height=setup._screen_height, 
                            caption=setup._game_name)
window.set_location(x=100, y=100)

#grous and batchs
GUI_group = glet.graphics.Group(order = 6)
tower_group = glet.graphics.Group(order = 5)
tower_group_radius = glet.graphics.Group(order = 4)
enemy_group = glet.shapes.Group(order = 3)
backgound_group = glet.shapes.Group(order = 0)

main_render_batch = glet.shapes.Batch()

#player
player = Player(game_difficulty=setup._game_difficulty, batch=main_render_batch, group=GUI_group)

 
#GUI
side_pannel = glet.shapes.Rectangle(x=setup._screen_width, 
                                    y=0, 
                                    width=setup._game_side_pannel,
                                    height=setup._screen_height,
                                    batch=main_render_batch, 
                                    group=GUI_group,
                                    color=(150, 200, 220))
tower_butten = myButton(batch=main_render_batch, group=GUI_group)

# maps
chossen_map = maps.List_of_game_maps[2]
lines = glet.shapes.MultiLine(coordinates=chossen_map['map_path'], thickness=setup._screen_width//30, color=chossen_map['path_color'], group=backgound_group, batch=main_render_batch)

#enemy
enemy_holder = enemy.Enemy_group(densetey=7)
enemy_holder.Auto_Fill_list(number_of_enemys= 15,
                           map=chossen_map['map_path'],
                           player=player,
                           gr_group=enemy_group,
                           gr_batch=main_render_batch)


# denne funktion biver kald for værd frame
@window.event
def on_draw() -> None:
   window.clear()
   main_render_batch.draw()

   #shapeBath.draw()
   #towerTank.draw()

@window.event
def on_mouse_motion(x: int, y: int, dx: int, dy: int) -> None:
   pass
   #print(x, y)

@window.event
def on_mouse_press(x: int, y: int, button: int, modifiers: int) -> None:
   tower_butten.on_mouse_press(x, y, button, modifiers)
   if tower_butten.toggle and tower_butten.place_tower(x, y):  
      try:
         player.add_tower(turret_1(
                           x=x,
                           y=y,
                           batch=main_render_batch,
                           group=tower_group,
                           group_gui=tower_group_radius
                        ), chossen_map['map_path'])
      except Exception as err:
         print(err)
      


# opdatere framens indhold
def update(dt):
   #towerTank.rotate(-5)
   enemy_holder.SendOut()
   player.Tower_update(dt=dt,enemy_list=enemy_holder.enemy_list)

   
# setter frame rate på 60 fps
glet.clock.schedule_interval(update, 1/10)
glet.app.run()
