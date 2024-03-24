from pyglet import app
from pyglet.window import Window 
from pyglet import shapes
from pyglet import clock

class Ball(shapes.Circle):
    dx = 0
    dy = 0
    elasticity = 1
    weight = 1

    def __init__(self, x, y, radius, dx, dy, elasticity, weight, color=..., batch=None, group=None):
        super().__init__(x, y, radius, None, color, batch, group)
        self.dx = dx
        self.dy = dy
        self.weight = weight
        self.elasticity = elasticity

    def is_below(self, y):
        return self.y - self.radius < y
    
    def is_left_of(self, x):
        return self.x + self.radius < x
    
    def is_right_of(self, x):
        return self.x - self.radius > x
    
def bind_to_window(ball: Ball):
    if ball.is_below(0):
        ball.dy = -ball.elasticity*ball.dy
    if ball.is_left_of(0) or ball.is_right_of(width):
        ball.dx = -ball.elasticity*ball.dx


width = 800
height = 800
window = Window(width, height)
ball1 = Ball(width//2, height//2, 20, 1, 0, 0.95, 1, (255, 0, 0))
dt = 1/120
G = 9.8

@window.event
def on_draw():
    window.clear()
    ball1.draw()

def update(dt):
    global ball1
    ball1.dy -= G*dt

    bind_to_window(ball1)

    ball1.x += ball1.dx
    ball1.y += ball1.dy

clock.schedule_interval(update, dt)
app.run() 