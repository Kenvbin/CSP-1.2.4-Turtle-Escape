import turtle as t
import random as r

lengthygenthy = 20
path_width = 20
t.pensize(10)
randomise = 5
t.speed(1)
randomgrandom = 5


def draw_doooooooooooooooor():
  global path_width, lengthygenthy, randomise
  randomise = 1
  t.penup()
  t.forward(path_width*2)
  t.pendown()



def spiralhal(howmany):
  global lengthygenthy, randomise, randomgrandom
  for i in range(howmany):
    if randomise <= 3:
      randomdorwego = r.randint(2,10)
      doorgoweee = lengthygenthy / randomdorwego
      t.forward(doorgoweee)
      draw_doooooooooooooooor()
      t.forward(lengthygenthy - (path_width*2) - doorgoweee)
    else:
      t.forward(lengthygenthy)
      wall_lore()
    t.right(90)
    lengthygenthy = lengthygenthy + 20
    randomise = r.randint(1,5)
    randomgrandom = r.randint(1,5)

def wall_lore():
  global randomgrandom
  randomgrandom = r.randint(1,5)
  if randomise > 3 and randomgrandom <= 3:
    t.right(90)
    t.forward(path_width * 2)
    t.backward(path_width * 2)
    t.left(90)

spiralhal(20)



wm = t.getscreen()
wm.mainloop()