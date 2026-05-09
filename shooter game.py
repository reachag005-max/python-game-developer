import pgzrun
import random

WIDTH=500
HEIGHT=400

turtle=Actor("turtle.png")
turtle.pos= 250,200

msg="best of luck"
score= 0

def draw():
    screen.fill("green")
    turtle.draw()
    screen.draw.text(("welcome to the shooter game, cilck on the villan to destroy him"),(10,50),color="black")
    screen.draw.text(msg,(100,375))
    screen.draw.text(f"score = {score}",(350,375))
    
def on_mouse_down(pos):
    global msg,score
    if turtle.collidepoint((pos)):
        turtle.x= random.randint(50,WIDTH-50)
        turtle.y= random.randint(50,HEIGHT-50)
        sounds.eep.play()
        msg="Good Shot"
        score+=5

    else:
        msg="You Missed"
        score-=2

pgzrun.go()