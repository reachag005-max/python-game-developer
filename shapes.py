import pgzrun

WIDTH=400
HEIGHT= 400

"""def draw():
    screen.fill("cyan")
    screen.draw.text(("HI"),(120,350),color="black")
    screen.draw.filled_circle((340,150),60,color="green")

    re = Rect((24,60),(50,40))
    screen.draw.rect(re,"blue")
    screen.draw.circle((350,250),17,color="red")"""



def draw():
    screen.fill("light blue")
    screen.draw.circle((200,200),120,color="red")
    screen.draw.circle((200,200),90,color="white")
    screen.draw.circle((200,200),60,color="red")
pgzrun.go()