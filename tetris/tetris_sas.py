from pyglet import app
from pyglet.window import Window 
from pyglet import image
from pyglet import clock
from random import randint, choice
from pyglet.window import key
import numpy as np

width = 300
height = 500
cell_size = 20
num_columns = width // cell_size
num_rows = height // cell_size

def new_shape(x, y, cell_size):
    return choice([
        new_fat_boi(x, y, cell_size),
        new_tall_boi(x, y, cell_size),
        new_big_foot(x, y, cell_size)
    ])

def new_fat_boi(x, y, cell_size):
     x = min(x, (num_columns-2)*cell_size)
     return [
          [x, y],
          [x+cell_size, y],
          [x, y+cell_size],
          [x+cell_size, y+cell_size]
          ]

def new_tall_boi(x, y, cell_size):
     x = min(x, (num_columns-2)*cell_size)
     return [
          [x, y],
          [x, y-1*cell_size],
          [x, y-2*cell_size],
          [x, y-3*cell_size]
          ]

def new_big_foot(x, y, cell_size):
     x = min(x, (num_columns-2)*cell_size)
     return [
          [x, y],
          [x, y-1*cell_size],
          [x, y-2*cell_size],
          [x+cell_size, y-2*cell_size]
          ]

board = np.full((num_columns, num_rows), False)
window = Window(width, height)
squares = new_shape(width- 2*cell_size, width- 2*cell_size, cell_size)

@window.event
def on_draw():
    window.clear()
    for x in range(len(board)):
         for y in range(len(board[x])):
              if board[x][y]:
                draw_square(x*cell_size, y*cell_size, cell_size, color = (255, 0, 0, 0))

    for sq in squares:
        draw_square(sq[0], sq[1], cell_size, color = (255, 0, 0, 0))

def draw_square(x, y, size, color=(255, 255, 255, 0)):
    img = image.create(size, size, image.SolidColorImagePattern(color))
    img.blit(x, y)

def update(dt):
    global squares
    needs_new_square= False
    for sq in squares:
        if sq[1] == 0:  
            needs_new_square= True
        if board[sq[0]//cell_size][(sq[1]//cell_size)-1]:
            needs_new_square=True

    if needs_new_square:
        for sq in squares:
            board[sq[0]//cell_size][sq[1]//cell_size] = True
        squares = new_shape(randint(1, window.width//cell_size)*cell_size-cell_size, window.height - cell_size, cell_size)
    else:
        for sq in squares:
            sq[1] -= cell_size

@window.event
def on_key_press(symbol, modifiers):
    global squares
    sq= squares[-1] 

    if symbol == key.LEFT:
        for sq in squares: 
            sq[0] = sq[0]-cell_size
    elif symbol == key.RIGHT:
        for sq in squares: 
            sq[0] = sq[0]+cell_size

clock.schedule_interval(update, 1/100)
app.run() 