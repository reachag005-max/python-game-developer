import pgzrun
import random

WIDTH = 400
HEIGHT = 600

ship = Actor("spaceship.png")
ship.x = WIDTH//2
ship.y = HEIGHT-70


aliens = []

bullets = []

direction = 1

score = 0

def drawscore():
    screen.draw.text(f"score : {score} ",(50,50))

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet.png"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y-25

for x in range(8):
    for y in range (4):
        aliens.append(Actor("alien.png"))
        aliens[-1].x = 100 + 50*x
        aliens[-1].y = 0 + 30*y

def update():
    global direction,score
    pass
    if keyboard.d:
        ship.x += 10
    if keyboard.a:
        ship.x -= 10
    for bullet in bullets:
        bullet.y-=10
    movedown = False
    if len(aliens)>0 and (aliens[-1].x>WIDTH-20 or aliens[-1].x<20):
        movedown = True
        direction = direction *-1
        for alien in aliens:
            alien.x += 2*direction
            if movedown == True:
                alien.y +=1

            for bullet in bullets:
                if alien.colliderect(bullet):
                    aliens.remove(alien)
                    bullets.remove(bullet)
                    score+=1

def draw():
    screen.fill("green") 
    ship.draw()
    for alien in aliens:
        alien.draw()
    for bullet in bullets:
        bullet.draw()
    drawscore()

pgzrun.go()