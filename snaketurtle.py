import turtle
import time
import random
#snake
snake = turtle.Turtle()
snake.shape("square")
snake.speed(0)
snake.shapesize(1)
snake.color("dark green")
turtle.bgcolor("light green")
snake.direction = "stop" 
snake.pensize(15)
snake.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.5)



def rando_food_loc():
     x = random.randint(-300, 300)
     y = random.randint(-300, 300)
     food.sety(y)
     food.setx(x)


def check_bounds(): 
    x = snake.xcor()
    y = snake.ycor()
    
    if x > 350:
        snake.setx(-350)
    elif x < -350:
        snake.setx(350)

    if y > 350:
        snake.sety(-350)
    elif y < -350:
        snake.sety(350)
window = turtle.Screen() #makes it in charge of the screen
window.tracer(0) #doesn't delay graphics from being updated

def set_up():
    snake.direction = "up" #whenever the function's called, snake direction is now up
def set_down():
    snake.direction = "down"
def set_left():
    snake.direction = "left"
def set_right():
    snake.direction = "right"
def pause():
    snake.direction = "stop"
    food.direction = "stop"
    snake_alive = False


#check if snake ate food
def ate_food(score):
    x = int(snake.xcor())
    y = int(snake.ycor())
    foodx = int(food.xcor())
    foody = int(food.ycor())
    xdiff = x - foodx
    ydiff = y - foody
    if abs(xdiff) <= 15 and abs(ydiff) <= 15:
        score += 1
        rando_food_loc()
        return True
    else: 
        return False

    
def move():
    x = snake.xcor()
    y = snake.ycor()
    
    if snake.direction == "up":
        snake.sety(y + 20)
        time.sleep(0.05)
    if snake.direction == "down":
        snake.sety(y - 20)
        time.sleep(0.05)
    if snake.direction == "right":
        snake.setx(x + 20)
        time.sleep(0.05)
    if snake.direction == "left":
        snake.setx(x - 20)
        time.sleep(0.05)
#score stuff
ref = turtle.Turtle()
ref.hideturtle()
ref.penup()
ref.goto(250, 250)
def display_score(score):
    ref.clear()
    ref.color("black")
    ref.write(f"score: {score}", font=("Times New Roman", 20))
#adding turtle
new_segments = []
length_of_snake = 1
def add_turtle():
    x = snake.xcor()
    y = snake.ycor()
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape('square')
    new_segment.goto(x,y)
    new_segment.penup()
    new_segments.append(new_segment)
        
    


#window

window.listen()
window.onkeypress(set_up, "w")  #(function, key)
window.onkeypress(set_down, "s")
window.onkeypress(set_left, "a")
window.onkeypress(set_right, "d")
window.onkeypress(pause, "p")


snake_alive = True
score = 0
rando_food_loc()
while snake_alive:
    window.update()
    move()
    check_bounds()
    if ate_food(score) == True:
        score += 1
        length_of_snake += 1
        print(score)
        display_score(score)
        #add_turtle()



    time.sleep(0.1) 

turtle.mainloop()