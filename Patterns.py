import pgzrun
import random

WIDTH=400
HIEGHT=400
 
"""def draw():
    w = WIDTH
    h = HIEGHT-300
    
    for i in range(20):
        r = 255
        g = 20
        b = random.randint(100,255)
        rect = Rect((0,0),(w,h))
        rect.center = (200,200)
        screen.draw.rect(rect,(r,g,b))

        w -= 10
        h += 10
        r -= 10
        g += 10"""

def draw():
    radius= 200

    for i in range (20):
        r = random.randint(20,220)
        g = random.randint(50,180)
        b = random.randint(100,255) 

        screen.draw.circle((200,200),radius,color=(r,g,b))

        radius -=10
        r -= 10
        g += 10


pgzrun.go()


