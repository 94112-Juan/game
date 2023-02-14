from random import randint
orange = Actor("orange")

def draw():
    screen.clear()
    orange.draw()

def place_orange( ):
    orange.x = randint(10, 800)
    orange.y = randint(10, 600)

def on_mouse_down(pos):
    if orange.collidepoint(pos):
        print("Good shot!")
        place_orange()
    else:
        print("You missed!")
        quit()


