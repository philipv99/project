#pyglet
import pyglet as glet
# genreic
import math
# my own
from buttens import myButton
from tower import Tank
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
tower_group = glet.graphics.Group(order = 3)
enemy_group = glet.shapes.Group(order = 4)
backgound_group = glet.shapes.Group(order = 0)

main_render_batch = glet.shapes.Batch()

#player
player = Player(game_difficulty=setup._game_difficulty, batch=main_render_batch, group=GUI_group)

#GUI
# laver objekter
#towerTank = Tank(400, 300)
side_pannel = glet.shapes.Rectangle(x=setup._screen_width, 
                                    y=0, 
                                    width=setup._game_side_pannel,
                                    height=setup._screen_height,
                                    batch=main_render_batch, 
                                    group=GUI_group,
                                    color=(150, 200, 220))
tower_butten = myButton(batch=main_render_batch, group=GUI_group)

# maps
chossen_map = maps.List_of_game_maps[3]
lines = glet.shapes.MultiLine(coordinates=chossen_map['map_path'], thickness=setup._screen_width//30, color=chossen_map['path_color'], group=backgound_group, batch=main_render_batch)

#enemy
number_of_enemys = 5
enemy_list = []
for num in range(0, number_of_enemys):
   enemy_list.append(enemy.Enemy(chossen_map['map_path'], speed= 3, player=player, damage= 1, group=enemy_group, batch=main_render_batch))

follow = False

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


@window.event
def on_mouse_press(x: int, y: int, button: int, modifiers: int) -> None:
   tower_butten.on_mouse_press(x, y, button, modifiers)


# opdatere framens indhold
def update(dt):
   #towerTank.rotate(-5)
   for enemy in enemy_list:
         enemy.move()
         

# setter frame rate på 60 fps
glet.clock.schedule_interval(update, 1/60)
glet.app.run()
