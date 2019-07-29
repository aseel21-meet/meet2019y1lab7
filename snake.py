import turtle #library
import random #later

turtle.tracer(1,0)#move more smootly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)#windo size

turtle.penup() #not darwing

SQUARE_SIZE=20 #variables for turtle apearence setting
START_LENGTH=6
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
    for  
    
    
    
    

turtle.mainloop()
