import turtle

score=0
def add_score():
    global score
    score +=1
    scoring=turtle.Turtle()
    scoring.penup()
    scorinng.goto(0,-400)
    scoring.pendown()
    scoring.write(score,align='center',move=False,font=('arial',18,'normal')
                 

turtle.mainloop()
