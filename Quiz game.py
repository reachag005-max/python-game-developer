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
question_file = "quest.txt"
marqueemsg = ""
ansboxes = [ansbox1,ansbox2,ansbox3,ansbox4]
questions = []
questindex = 0
questcount = 0
isgameover = False
score = 0

marqueebox.move_ip(0,0)
questionbox.move_ip(10,80)
timebox.move_ip(470,80)
ansbox1.move_ip(10,160)
ansbox2.move_ip(210,160)
ansbox3.move_ip(10,280)
ansbox4.move_ip(210,280)
skipbox.move_ip(400,160)

def load_question():
    global questions,questcount

    with open(question_file, "r") as file:
       questions = file.readlines()
    print(questions)

    questcount = len(questions)

def move_marquee():
    marqueebox.x -= 2
    if marqueebox.right < 0:
        marqueebox.left = WIDTH

def read_questfile():
    global questcount, questions
    qfile= open("quest.txt","r")
    for question in qfile:
        questions.append(question)
        questcount= questcount+1

    qfile.close()

def read_nextquest():
    global questindex
    questindex = questindex+1
    return questions.pop(0).split(",")

def gameover():
    global time,questions,isgameover,score
    message = f"Gameover \n You scored: {score} questions correct"
    questions = [message,"-","-","-","-",1]
    time = 0
    isgameover = True

def skip_quest():
    global time,questions
    if questions and not isgameover:
        questions = read_nextquest()
    else:
        gameover()

def update_timeleft():
    global time 
    if time :
        time= time-1
    else:
        gameover()

def correct_ans():
    global time,question,score,questions
    score +=1 
    if questions:
        question = read_nextquest()
        time = 10
    else:
        gameover()


def on_mouse_down(pos):
    index = 1
    for box in ansboxes:
        if box.collidepoint(pos):
            if index is int(questions[5]):
                correct_ans()
            else:
                gameover()
        index = index + 1
    if skipbox.collidepoint(pos):
        skip_quest()
    
    

    
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
    marqueemsg = marqueemsg + f" Q {questindex} of {questcount}"
    screen.draw.textbox(marqueemsg,marqueebox,color = "white")
    screen.draw.textbox(str(time),timebox,color = "white",shadow = (0.5,0.5),scolor = "Grey")
    screen.draw.textbox("SKIP",skipbox,color="Black",angle = 90)
    screen.draw.textbox(questions[0].strip(),questionbox,color = "black",shadow = (0.5,0.5),scolor= "Grey")
    index = 1
    for ansbox in ansboxes:
        screen.draw.textbox(questions[index].strip(),ansbox,color="black")
        index += 1

def update():
    move_marquee()   
read_questfile()
questions = read_nextquest()
#load_question()
pgzrun.go()