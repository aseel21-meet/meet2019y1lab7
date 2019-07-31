import turtle #library
import random #later

turtle.tracer(1,0)#move more smootly

SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X,SIZE_Y)#windo size

SIZE_X_game=600
SIZE_Y_game=600
#turtle.setup(SIZE_X_game,SIZE_Y_game)

turtle.penup() #not darwing

SQUARE_SIZE=20 #variables for turtle apearence setting
START_LENGTH=9
TIME_STEP=100
score=0
#turtle.register_shape('sand.gif')
#turtle.bgpic('sand.gif')

pos_list=[]
stamp_list=[]
food_pos=[]
food_stamp=[] #making new lists=organizing

snake=turtle.clone() #starts at (x,y)were the original turtle is
snake.shape('square')

turtle.hideturtle() #original turtle invisible on screen

def new_stamp():
    snake_pos=snake.pos() # the  current position  is now in this variable
    pos_list.append(snake_pos) #prev variable added to the list
    id1=snake.stamp() #puts a stamp on it 
    stamp_list.append(id1) #added the stanp to a list -rn index [0]
for num_piece in range(START_LENGTH): #anything defined  in a function cant be used outside &anything defined out of  (before) it can be used in the function
    x_pos=snake.pos()[0] #defining variables-that  taake an indexed int from a position tuple with 2 length
    y_pos=snake.pos()[1]
    x_pos +=SQUARE_SIZE #20 units is added to the value of the x cor
    snake.goto(x_pos,y_pos)
    new_stamp()
#part 2
def remove_tail():
    old_stamp=stamp_list.pop(0) #the last piece of tail-our first stamp will show in the shell and then get deleted fromthe list
    snake.clearstamp(old_stamp) #the stamp we deleted from the list will not aper on turtle window anymore
    pos_list.pop(0)             #we delte the first position that was stored in the list-the last tail -pops on shellscore=0

        
    
    #global score
    #score +=1
    #scoring=turtle.Turtle()
    #scoring.penup()
    #scorinng.goto(0,-400)
    #scoring.pendown()
    #scoring.write(score,align='center',move=False,font=('arial',18,'normal'))




snake.direction='up' #variable for up string :t we have a variable we can change the value of in the functiono make sure
UP_EDGE=300
DOWN_EDGE=-300
RIGHT_EDGE=300
LEFT_EDGE=-300

border=turtle.Turtle()
border.penup()
border.goto(300,-300)
border.pendown()
border.goto(300,300)
border.goto(-300,300)
border.goto(-300,-300)
border.goto(300,-300)
border.penup()
border.goto(0,400)
border.pendown
border.color('green')
border.write('snake game',align='center',move=False,font=("arial",18,'normal'))
border.hideturtle()


def up(): #new function called up
    snake.direction="up" #change your direction to up
    #move_snake() # the drawing-start moving up
    print('you pressed the up button')
    
def down(): #new function called up
    snake.direction="down" #change your direction to down
    #move_snake() # the drawing-start moving down
    print('you pressed the down button')
    
def left(): #new function called left
    snake.direction="left" #change your direction to left
    #move_snake() #the drawing-start moving to the left
    print('you pressed the left button')
    
def right(): #new function called right
    snake.direction="right" #change your direction to the right
    #move_snake() #updeta the drawing-start moving right
    print('you pressed the right button')




turtle.onkeypress(up,'Up')#when we press the key that the comouter knows as the string up you do the function that is called up
turtle.onkeypress(down,'Down')
turtle.onkeypress(left,'Left')
turtle.onkeypress(right,'Right')
turtle.listen() #when i press on one of those keys ypou listen and do the next functions

turtle.register_shape('trash.gif')#we add a trash pic to the folder and it adds it tp the turtle window
food=turtle.clone()
food.shape('trash.gif')
food_pos=[]
food_stamp=[]
for this_food_pos in food_pos:
    food.penup()
    food.goto(this_food_pos)
    foodid1=food.stamp()
    food_stamp.append(foodid1)

    
scoring=turtle.Turtle()
scoring.penup()
scoring.goto(0,-400)
scoring.pendown()
scoring.hideturtle()

def move_snake():
    my_pos=snake.pos() #the position where i am now is stored here in the function only)
    x_pos=my_pos[0]
    y_pos=my_pos[1] #variables to help us change directions
    if snake.direction=='up': #if you pressed up the up function will start and accordig to that it will be true
        snake.goto(x_pos,y_pos+SQUARE_SIZE) #adding units to the y so it goes higher in the y 
        print('you moved up')
    elif snake.direction=='down':
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print('you moved down')
    elif snake.direction=='left':
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print('you moved left')
    elif snake.direction=='right':
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]
    if new_x_pos==UP_EDGE:
        print('you hit the up edge,geme over')
        quit()
    elif new_x_pos==DOWN_EDGE:
        print('you hit the down edge,geme over')
        quit()
    elif new_x_pos==RIGHT_EDGE:
        print('you hit the right edge,geme over')
        quit()
    elif new_x_pos==LEFT_EDGE:
        print('you hit the left edge,geme over')
        quit() #closes the program

    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #the position where thefood is now is same as the position of the snake position
        food.clearstamp(food_stamp[food_index]) #removes  the current food stamp from the list
        food_pos.pop(food_index) #the current position will popon the shell and get deleted from the list
        food_stamp.pop(food_index)
        print('you have eaten the food')
        id3=food.pos()
        stamp_list.append(id3[-1])
        print('you have grown a bit')
        #challenge
        
        
                #for score in range ():
        
        global score
        score +=1
        scoring.clear()
        #scoring.color('green')
        scoring.write(score,align='center',move=False,font=('Arial',18,'normal'))
        #scoring.clear()

        print('you scored yeyyyyyyyyyyyyyyyyy')
        #scoring.color(turtle.bgcolor())

        #scoring.clear()

    
        
    if snake.pos() in pos_list:
        print('you thouched')
        quit()
        
        
        
        
    turtle.ontimer(move_snake,TIME_STEP) #keeps moving once starting
    #two argunmwnts-inputs, waits for an amount of time AND CALLS OUR MOVE_SNAKE FUNCTION
    new_stamp()
    remove_tail()
    if len (food_stamp)<=6:
        make_food()
    #8if pos_list[0]==pos_list[1: ]:
       #8 print('your head touched your body')
        #8quit()
   #8else:
       #8 print('didnt touch the head')
       
    
def make_food():
    print('lets make food')
   # min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
   # max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    #min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
   # max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    min_x=-int(SIZE_X_game/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X_game/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y_game/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y_game/2/SQUARE_SIZE)-1
    
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE #picks randomly a number between the values we set before for point sthat are on the screen
    food.goto(food_x,food_y)
    food_pos.append((food_x,food_y))
    foodid2=food.stamp()
    food_stamp.append(foodid2)
    
       


move_snake()




#score=0
#def add_score():
    #global score
    #score +=1
    #scoring=turtle.Turtle()
    #scoring.penup()
    #scorinng.goto(0,-400)
    #scoring.pendown()
    #scoring.write(score,align='center',move=False,font=('arial',18,'normal'))
    


    
    
    
        
    
    




        
        
    
    

    








turtle.mainloop()
