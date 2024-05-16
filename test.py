import pyglet as glet
from tower import Tower_1_test


window = glet.window.Window(width=500,
                              height=500,
                              caption="test")

t = Tower_1_test(x= 200 , y= 200)


@window.event
def on_draw() -> None:
   window.clear()
   t.draw()

def update(dt):
   t.rotation += 2

glet.clock.schedule_interval(update, 1/60)
glet.app.run()