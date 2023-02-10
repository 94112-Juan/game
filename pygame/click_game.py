stick = Actor('charater')
stick.topright = 0, 10

WIDTH=500
HEIGHT= stick.height + 50

def draw():
    screen.clear()
    stick.draw()

def update():
    stick.left = stick.left +2
    if stick.left>WIDTH:
        stick.right=0
