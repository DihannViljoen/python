from pyglet import app
from pyglet.window import Window 
from pyglet import image
from pyglet import clock
from pyglet.window import key
from pyglet import graphics
from pyglet import media
from pyglet import text
from itertools import cycle 
from random import randint

window = Window(500, 500)

@window.event
def on_draw():
    window.clear()
    draw_square(fd_x, fd_y, cell_size, color = (255, 0, 0, 0))
    for coords in tail:
        draw_square(coords[0], coords[1], cell_size, color = (127, 127, 127, 0))
    draw_square(snk_x, snk_y, cell_size)


def draw_square(x, y, size, color=(255, 255, 255, 0)):
    img = image.create(size, size, image.SolidColorImagePattern(color))
    img.blit(x, y)
    if game_over:
        draw_game_over()

def new_game():
    global snk_x, snk_y, snk_dx, snk_dy, game_over
    reset_snake()
    place_food()
    game_over=False
    if cell_size < 1 or window.width % cell_size != 0 or window.height % cell_size != 0:
        print("error: Snake size must be greater than 0 and must devide the window width and window heifht exactly")
        exit()
def place_food():
    global fd_x, fd_y
    fd_x = randint(0, (window.width // cell_size)-1)* cell_size 
    fd_y = randint(0, (window.height // cell_size)-1)* cell_size 

def draw_game_over():
    game_over_screen = text.Label(f'Score: {len(tail)}\n(press space to restart)',font_size=24,
                                    x=window.width//2, y=window.height//2, width=window.width, align='center',
                                       anchor_x='center', anchor_y='center', multiline=True)
    game_over_screen.draw()

@window.event
def on_key_press(symbol, modifiers):
    global snk_dx, snk_dy, game_over
    if game_over and symbol == key.SPACE:
        new_game() 

    if symbol == key.LEFT: 
        if not snk_dx == 1 * cell_size:
            snk_dx = -cell_size
            snk_dy = 0
    elif symbol == key.RIGHT:
        if not snk_dx == -1 * cell_size:
            snk_dx = cell_size
            snk_dy = 0
    elif symbol == key.UP:
        if not snk_dy == -1 * cell_size:
            snk_dx = 0
            snk_dy = cell_size
    elif symbol == key.DOWN:
        if not snk_dy == 1 * cell_size:
            snk_dx = 0
            snk_dy = -cell_size

def update(dt):
    global snk_x, snk_y, fd_x, fd_y, game_over 
    if game_over:
        return
    if game_over_condition():
        game_over = True    
        return

    tail.append((snk_x, snk_y))
    snk_x += snk_dx
    snk_y += snk_dy

    if snk_x == fd_x and snk_y ==fd_y:
        place_food()
    else:
        tail.pop(0)

def game_over_condition():
    condition1 = snk_x + snk_dx < 0 or snk_x + snk_dx > window.width - cell_size or snk_y + snk_dy <0 or snk_y + snk_dy > window.height - cell_size
    condition2 = (snk_x, snk_y) in tail 
    return condition1 or condition2

def reset_snake():
    global snk_x, snk_y, snk_dx, snk_dy, tail
    snk_x= window.width // cell_size // 2 * cell_size
    snk_y= window.height // cell_size // 2 * cell_size
    snk_dx, snk_dy = 0, 0
    tail = []

cell_size = 20
    
snk_dx, snk_dy = 0, 0

snk_x= window.width // cell_size // 2 * cell_size
snk_y= window.height // cell_size // 2 * cell_size
    
fd_x, fd_y = 0, 0
place_food()
tail = []
game_over = False 
clock.schedule_interval(update, 1/15)
app.run()
