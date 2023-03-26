from pygame import *

back = (250,180,180)
win_width = 600
win_heigth = 500
window = display.set_mode((win_width,win_heigth))
window.fill(back)

clock = time.Clock()

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)