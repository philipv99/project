#pyglet
import pyglet as glet
from pyglet import shapes
from pyglet import gui
from pyglet import text
from pyglet.math import Vec2

# genreic
import math
# my own
from Towers import Tank
import setup
from player import Player


# laver  vinduer til at havde spillet i.
window = glet.window.Window(width=setup._screen_width, 
                            height=setup._screen_height, 
                            caption=setup._game_name)
window.set_location(x=100, y=100)

#player
player = Player(game_difficulty=setup._game_difficulty)

#GUI
# laver objekter
shapeBath = glet.graphics.Batch()
Ellipsi = glet.shapes.Ellipse(x=1000, y= 200, a=79, b=45, color=(255, 34, 255), batch=shapeBath)
star = glet.shapes.Star(x=800, y=550, inner_radius=80, outer_radius=100, num_spikes=8, color=(50, 255, 255), batch=shapeBath)
towerTank = Tank(400, 300)

Map_wayPoints = [
   Vec2(2, 2),
   Vec2(4, 6),
   #Vec2(400, 600),
   # Vec2(200, 300)
]

#line = glet.shapes.MultiLine(Map_wayPoints)



# detnne funktion lbiver kald for værd frame
@window.event
def on_draw() -> None:
   window.clear()
   
   shapeBath.draw()
   towerTank.draw()

   player.draw()

@window.event
def on_mouse_motion(x: int, y: int, dx: int, dy: int) -> None:
   Ellipsi.position = (x, y)

@window.event
def on_mouse_press(x: int, y: int, button: int, modifiers: int) -> None:
   star.position = (x, y)

value = 0
# opdatere framens indhold
def update(dt):
   global value
   value += 0.05
   star.inner_radius += math.sin(value) * 1.2
   towerTank.rotate(-5)

# setter frame rate på 60 fps
glet.clock.schedule_interval(update, 1/120)
glet.app.run()
