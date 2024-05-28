import pyglet as glet

window = glet.window.Window(width=500,
                              height=500,
                              caption="test")

v = "noget"
def t(te):
   if te == None:
      te = "noget"
   else: 
      te = None
   print(te)
   

@window.event
def on_draw() -> None:
   window.clear()

def update(dt):
   t(v)

glet.clock.schedule_interval(update, 1/1)
glet.app.run()