#pyglet
import pyglet as glet
# my own
import buttens
from tower import *
import setup
import maps
from player import Player
import enemy


#* ------------------ laver  vinduer til at havde spillet i. ------------------ #
window = glet.window.Window(width=setup._screen_width + setup._game_side_pannel, 
                            height=setup._screen_height, 
                            caption=setup._game_name)
window.set_location(x=100, y=100)

#* ----------------------------- grous and batchs ----------------------------- #
Game_overlay_group = glet.graphics.Group(order = 6)

GUI_group = glet.graphics.Group(order = 5)
tower_group = glet.graphics.Group(order = 4)
tower_group_radius = glet.graphics.Group(order = 3)
enemy_group = glet.shapes.Group(order = 2)
backgound_group = glet.shapes.Group(order = 0)

Game_overlay_batch = glet.graphics.Batch()
main_render_batch = glet.graphics.Batch()

#? ---------------------------------- player ---------------------------------- #
player = Player(game_difficulty = setup._game_difficulty, 
                gameover_group  = Game_overlay_group, 
                gameover_batch  = Game_overlay_batch,
                batch           = main_render_batch, 
                group           = GUI_group)


#* ------------------------------------ GUI ----------------------------------- #
side_pannel = glet.shapes.Rectangle(x=setup._screen_width, 
                                    y=0, 
                                    width=setup._game_side_pannel,
                                    height=setup._screen_height,
                                    batch=main_render_batch, 
                                    group=GUI_group,
                                    color=(150, 200, 220))
tower_button = buttens.turret_button(batch=main_render_batch, group=GUI_group)
tower2_button = buttens.turret_button( x = setup._screen_width  + (setup._game_side_pannel // 6 ) * 3,
                                       y=(setup._screen_height // 12) * 10, 
                                      batch=main_render_batch, group=GUI_group)

#* ----------------------------------- maps ----------------------------------- #
chossen_map = maps.List_of_game_maps[1]
lines = glet.shapes.MultiLine(coordinates=chossen_map['map_path'], thickness=setup._screen_width//30, color=chossen_map['path_color'], group=backgound_group, batch=main_render_batch)

#! ----------------------------------- enemy ---------------------------------- #
enemy_holder = enemy.Enemy_group(player=player, round=player._Round, map=chossen_map['map_path'], gr_batch= main_render_batch, gr_group=enemy_group)
#& ----------------- denne funktion biver kald for værd frame ----------------- #
@window.event
def on_draw() -> None:
   window.clear()
   main_render_batch.draw()

   if player.loost_game == True:
      Game_overlay_batch.draw()

#& ----------------------- event tricker for musse klik ----------------------- #
@window.event
def on_mouse_press(x: int, y: int, button: int, modifiers: int) -> None:
   speed_button.on_mouse_press(x, y, button, modifiers)

   tower_button.on_mouse_press(x, y, button, modifiers)
   if tower_button.toggle and tower_button.place_tower(x, y):  
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
   
   tower2_button.on_mouse_press(x, y, button, modifiers)
   if tower2_button.toggle and tower2_button.place_tower(x, y):  
      try:
         player.add_tower(turret_2(
                           x=x,
                           y=y,
                           batch=main_render_batch,
                           group=tower_group,
                           group_gui=tower_group_radius
                        ), chossen_map['map_path'])
      except Exception as err:
         print(err)

#& ------------------------- opdatere framens indhold ------------------------- #
def update(dt):
   enemy_holder.update()
   player.Tower_update(enemy_list=enemy_holder)

   if player.loost_game == True:
      glet.clock.unschedule(update)

   
#& ------------------------ setter frame rate på 60 fps ----------------------- #
def speed_value(value) -> None:
   if value == True:
      print("speed")
      glet.clock.unschedule(update)
      glet.clock.schedule_interval(update, 1/120)   
   else:
      print("slow")
      glet.clock.unschedule(update)
      glet.clock.schedule_interval(update, 1/60)
speed_button = buttens.Speed_button(func=speed_value,batch=main_render_batch, group=GUI_group)
glet.app.run()
