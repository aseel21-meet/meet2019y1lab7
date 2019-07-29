import turtle #library
import random #later

turtle.tracer(1,0)#move more smootly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)#windo size

turtle.penup() #not darwing

SQUARE_SIZE=20 #variables for turtle apearence setting
START_LENGTH=9
TIME_STEP=100

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
    pos_list.pop(0)             #we delte the first position that was stored in the list-the last tail -pops on shell
 
snake.direction='up' #variable for up string :t we have a variable we can change the value of in the functiono make sure
def up(): #new function called up
    snake.direction="up" #change your direction to up
    move_snake() # the drawing-start moving up
    print('you pressed the up button')
    
def down(): #new function called up
    snake.direction="down" #change your direction to down
    move_snake() # the drawing-start moving down
    print('you pressed the down button')
    
def left(): #new function called left
    snake.direction="left" #change your direction to left
    move_snake() #the drawing-start moving to the left
    print('you pressed the left button')
    
def right(): #new function called right
    snake.direction="right" #change your direction to the right
    move_snake() #updeta the drawing-start moving right
    print('you pressed the right button')

turtle.onkeypress(up,'Up')#when we press the key that the comouter knows as the string up you do the function that is called up
turtle.onkeypress(down,'Down')
turtle.onkeypress(left,'Left')
turtle.onkeypress(right,'Right')
turtle.listen() #when i press on one of those keys ypou listen and do the next functions

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
move_snake()
        
        
    
    

    








turtle.mainloop()
