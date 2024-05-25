import pyglet as glet

window = glet.window.Window(width=500,
                              height=500,
                              caption="test")

r = range(10, 20)
r2 = range(30, 10)

pointx = 11
pointy = 17

if r.count(pointx) > 0 and r2.count(pointy) > 0:
   print("in coord")

@window.event
def on_draw() -> None:
   window.clear()

def update(dt):
   pass

glet.clock.schedule_interval(update, 1/60)
glet.app.run()