import pgzrun
import random

WIDTH = 400
HEIGHT = 600

ship = Actor("spaceship.png")
ship.x = WIDTH//2
ship.y = HEIGHT-70


aliens = []

for x in range(8):
    for y in range (4):
        aliens.append(Actor("alien.png"))
        aliens[-1].x = 100 + 50*x
        aliens[-1].y = 0 + 30*y

def update():
    pass

def draw():
    screen.fill("green")
    ship.draw()
    for alien in aliens:
        alien.draw()

pgzrun.go()
