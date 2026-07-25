import pgzrun

TITLE = "quiz master "
WIDTH = 600
HEIGHT = 400

marqueebox = Rect(0,0,580,50)
questionbox = Rect(0,0,450,70)
timebox = Rect(0,0,50,70)
ansbox1 = Rect(0,0,180,90)
ansbox2 = Rect(0,0,180,90)
ansbox3 = Rect(0,0,180,90)
ansbox4 = Rect(0,0,180,90)
skipbox = Rect(0,0,70,180)

time = 10
question_file = ""
marqueemsg = ""
ansboxes = [ansbox1,ansbox2,ansbox3,ansbox4]
question = []
questindex = 0
questcount = 0
isgameover = False

marqueebox.move_ip(0,0)
questionbox.move_ip(10,80)
timebox.move_ip(470,80)
ansbox1.move_ip(10,160)
ansbox2.move_ip(210,160)
ansbox3.move_ip(10,280)
ansbox4.move_ip(210,280)
skipbox.move_ip(400,160)

def draw():
    global marqueemsg
    screen.clear()
    screen.fill ( color = "black")
    screen.draw.filled_rect(marqueebox,"black")
    screen.draw.filled_rect(questionbox,"lightblue")
    screen.draw.filled_rect(timebox,"lightblue")
    screen.draw.filled_rect(skipbox,"orange")
    for ansbox in ansboxes:
        screen.draw.filled_rect(ansbox,"red")
    marqueemsg = "Welcome to Quiz Master"

pgzrun.go()