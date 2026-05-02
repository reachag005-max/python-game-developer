import pgzrun

WIDTH=400
HIEGHT=400

def draw():
   screen.fill("light blue")
   screen.draw.filled_circle((200,200),100,color="yellow") 
   screen.draw.filled_circle((175,175),10,color="white")
   screen.draw.filled_circle((175,175),5,color="black") 
   screen.draw.filled_circle((250,175),10,color="white")
   screen.draw.filled_circle((250,175),5,color="black")
   screen.draw.filled_circle((200,250),15,color="black") 
   screen.draw.text(("Shocked Emoji"),(75,50),color="black")




pgzrun.go()