import pgzrun
import random

HEIGHT= 500
WIDTH= 600


sheep=Actor("sheep.png")
sheep.pos=150,200

wolf=Actor("wolf.png")
wolf.pos=225,200


score = 0
def draw():
    screen.blit("bg ",(0,0))
    sheep.draw()
    wolf.draw()
    screen.draw.text("chase that sheep!!!",(75,50),color="black")
    screen.draw.text(f"score ={score}",(300,50),color="black")
    



def update():
    if keyboard.w:
        wolf.y -= 3
    if keyboard.s:
        wolf.y += 3
    if keyboard.d:
        wolf.x += 3
    if keyboard.a:
        wolf.x -= 3
    global score
    if sheep.colliderect(wolf):       
        sheep.x= random.randint(50,WIDTH-50)
        sheep.y= random.randint(50,HEIGHT-50)
        score += 1
        sounds.sheep.play()




pgzrun.go()