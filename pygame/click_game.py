ghost = Actor('ghost')
ghost.topright = 0, 10

WIDTH=500
HEIGHT= ghost.height + 50

def draw():
    screen.clear()
    ghost.draw()

def update():
    ghost.left =ghost.left +2
    if ghost.left>WIDTH:
        ghost.right=0
def on_mouse_down(pos):
    if ghost.collidepoint(pos):
        sounds.ghostnoise.play()
        ghost.image='ghost_suprised'
