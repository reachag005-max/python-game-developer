import pgzrun
import random
from time import time

WIDTH=500
HEIGHT=400

numb=10
tow=[]
lines=[]
next=0
gametime=15
start_time= time()
gameover= False
won = False

for i in range(numb):
    tower=Actor("tower.png")
    tower.x=random.randint(50,WIDTH-50)
    tower.y=random.randint(50,HEIGHT-50)
    tow.append(tower)



def draw():
    screen.blit("map.png",(0,0))
    screen.draw.text("Conecting towers",(WIDTH//2,20),fontsize=40, color="black")
    number=1
    for i in tow:
       i.draw()
       screen.draw.text(str(number),(i.x,i.y+15),color="black")
       number+=1
    for line in lines:
        screen.draw.line(line[0],line[1],(0,0,0))
    if not gameover:
        remaining = max (0,gametime-int(time()-start_time))
        screen.draw.text(f"Time left: "+str(remaining),(20,20),fontsize=40, color = " brown")
    if gameover:
        if won:
            screen.draw.text("YOU WON!!!!",center = (WIDTH//2,HEIGHT//2),fontsize=70,color=" dark green")
        else:
            screen.draw.text("Time is up!!!!",center = (WIDTH//2,HEIGHT//2),fontsize=70,color="red")

def update():
    global gameover
    if not gameover:
        if time()-start_time >= gametime:
            gameover = True



def on_mouse_down(pos):
    global next,tow,lines,gameover,won
    if gameover:
        return
    if tow[next].collidepoint(pos):
        if next>0:
            lines.append((tow[next-1].pos,tow[next].pos))
        next += 1
        if next == numb:
            won = True
    else:
        lines=[]
        next=0

pgzrun.go()