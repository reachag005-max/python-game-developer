import pgzrun
import random

WIDTH = 400
HEIGHT = 600

ship = Actor("spaceship.png")
ship.x = WIDTH//2
ship.y = HEIGHT-70

meteors= []

aliens = []

bullets = []

direction = 1
directionm = 1

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

for x in range(8):
    for y in range(4):
        meteors.append(Actor("meteor.png"))
        meteors[-1].x = random.randint(100,WIDTH)
        meteors[-1].y = 0 + 30*y

def update():
    global direction,score,directionm
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
    movedown1= False
    if len(meteors)>0 and (meteors[-1].x>WIDTH-20 or meteors[-1].x<20):
        movedown1 = True
        directionm = directionm *-1
        for meteor in meteors:
            meteor.x += 2*directionm
            if movedown1 == True:
                meteor.y +=5

        for bullet in bullets: 
            if meteor.colliderect(bullet):
                meteors.remove(meteor)
                bullets.remove(bullet)
                score+=1

def draw():
    screen.fill("grey") 
    ship.draw()
    for alien in aliens:
        alien.draw()
    for bullet in bullets:
        bullet.draw()
    for meteor in meteors:
        meteor.draw()
    drawscore()
    if score == 28:
        screen.draw.text(("YOU WIN!!!"),(100,300),fontsize = 70 ,color="Green")


pgzrun.go()
