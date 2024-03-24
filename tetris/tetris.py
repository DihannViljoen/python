from pyglet import app
from pyglet.window import Window 
from pyglet import image
from pyglet import clock
from random import randint, choice
from pyglet.window import key
import numpy as np

width = 400
height = 600
window = Window(width, height)
cell_size = 20
num_columns = width // cell_size
num_rows = height // cell_size
board = np.empty((num_columns, num_rows), dtype=object)

class Shape:
    blocks = []
    color = (255, 0, 0)

def new_shape(x, y, cell_size):
     return choice([
     two_by_two(x, y, cell_size),
     l_long(x, y, cell_size),
     l_short_right(x, y, cell_size),
     l_short_left(x, y, cell_size),
     short_pp(x, y ,cell_size),
     lightning(x, y, cell_size)])

def two_by_two(x, y, cell_size):
     x = min(x, (num_columns-2)*cell_size)
     tbt = Shape()
     tbt.blocks = [
        [x, y],
        [x+cell_size, y],
        [x, y+cell_size],
        [x+cell_size, y+cell_size],
        ]
     tbt.color = (0, 255, 0, 0)
     
     return tbt

def l_long(x, y, cell_size):
    x = min(x, (num_columns-2)*cell_size)
    l_lg = Shape()
    l_lg.blocks= [       
        [x, y],
        [x, y-1*cell_size],
        [x, y-2*cell_size],
        [x, y-3*cell_size]
        ]
    
    l_lg.color= (255, 0, 0, 0)

    return l_lg

def l_short_right(x, y, cell_size):
    x = min(x, (num_columns-2)*cell_size)
    l_s_r = Shape()
    l_s_r.blocks= [
        [x, y],
        [x, y-1*cell_size],
        [x, y-2*cell_size],
        [x+cell_size, y-2*cell_size]
        ]
    
    l_s_r.color= (255, 255, 0, 0)

    return l_s_r

def l_short_left(x, y, cell_size):
    x = min(x, (num_columns-2)*cell_size)
    l_s_l = Shape()
    l_s_l.blocks= [
        [x, y],
        [x, y-1*cell_size],
        [x, y-2*cell_size],
        [x-cell_size, y-2*cell_size]]

    l_s_l.color= (255, 0, 255, 0)
    
    return l_s_l

def short_pp(x, y ,cell_size):
    x = min(x, (num_columns-2)*cell_size)
    s_pp = Shape()
    s_pp.blocks= [
        [x, y],
        [x, y-1*cell_size],
        [x-1*cell_size, y-1*cell_size],
        [x+1*cell_size, y-1*cell_size]
        ]
    s_pp.color= (0, 0, 255, 0)

    return s_pp

def lightning(x, y, cell_size):
    x = min(x, (num_columns-2)*cell_size)
    lg = Shape()
    lg.blocks= [
        [x, y],
        [x, y-1*cell_size],
        [x-1*cell_size, y-1*cell_size],
        [x-1*cell_size, y-2*cell_size]
    ]

    lg.color= (255, 0, 255, 0)

    return lg

shape = new_shape(width- 2*cell_size, width- 2*cell_size, cell_size)


@window.event
def on_draw():
    window.clear()
    for x in range(len(board)):
         for y in range(len(board[x])):
              if board[x][y]:
                draw_square(x*cell_size, y*cell_size, cell_size, color = board[x][y])

    for sq in shape.blocks:
        draw_square(sq[0], sq[1], cell_size, color = shape.color)

def draw_square(x, y, size, color=(255, 255, 255, 0)):
    img = image.create(size, size, image.SolidColorImagePattern(color))
    img.blit(x, y)

def update(dt):
    global shape
    needs_new_square= False
    for sq in shape.blocks:
        if sq[1] == 0:  
            needs_new_square= True
        if board[sq[0]//cell_size][(sq[1]//cell_size)-1]:
            needs_new_square=True

    if needs_new_square:
        for sq in shape.blocks:
            board[sq[0]//cell_size][sq[1]//cell_size] = shape.color
        shape = new_shape(randint(1, window.width//cell_size)*cell_size-cell_size, window.height - cell_size, cell_size)
    else:
        for sq in shape.blocks:
            sq[1] -= cell_size

@window.event
def on_key_press(symbol, modifiers):
    global shape

    if symbol == key.LEFT:
        for sq in shape.blocks: 
            sq[0] = sq[0]-cell_size
    elif symbol == key.RIGHT:
        for sq in shape.blocks:
            if not sq[0] + cell_size < width:
                return 
        for sq in shape.blocks: 
                sq[0] = sq[0]+cell_size

clock.schedule_interval(update, 1/10)
app.run() 