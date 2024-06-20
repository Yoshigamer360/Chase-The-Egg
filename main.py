# Chase the egg
# Created by: Yoshi gamer 360

import turtle, random, time

# Set up the screen
screen = turtle.Screen()
width = 500
height = 500
screen.setup(width, height)
screen.bgcolor('black')
screen.title('Hungry Turtle Game by Yoshi Gamer 360')

# Create player turtle
player = turtle.Turtle()
player.shape('turtle')
player.color('blue')
colour = ['green, blue, purple']
player.penup()

player2 = turtle.Turtle()
player2.shape('turtle')
player2.color('blue')
player2.penup()
player2.setheading(180)

# Create the food turtle
food = turtle.Turtle()
food.shape('circle')
food.color('yellow')
food.penup()
food.goto(random.randint((-width/2)+10, (width/2)-10),
          random.randint((-height/2)+10, (height/2)-10))


# Create the score turtle
score = turtle.Turtle()
score.shape('circle')
score.color('white')
score.hideturtle()
score.penup()
score.goto((-width/2)+10, (height/2)-30)
score.write('Score: 0', align='left', font=('Courier', 18, 'normal'))

score2 = turtle.Turtle()
score2.shape('circle')
score2.color('white')
score2.hideturtle()
score2.penup()
score2.goto((-width/2)+10, (height/2)-495)
score2.write('Score: 0', align='left', font=('Courier', 18, 'normal'))

# Set up the key bindings
def go_up():
    player.setheading(90)

def go_down():
    player.setheading(270)

def go_left():
    player.setheading(180)

def go_right():
    player.setheading(0)

def go_up2():
    player2.setheading(90)

def go_down2():
    player2.setheading(270)

def go_left2():
    player2.setheading(180)

def go_right2():
    player2.setheading(0)

screen.onkeypress(go_up, 'Up')
screen.onkeypress(go_down, 'Down')
screen.onkeypress(go_left, 'Left')
screen.onkeypress(go_right, 'Right')
screen.listen()

screen.onkeypress(go_up2, 'w')
screen.onkeypress(go_down2, 's')
screen.onkeypress(go_left2, 'a')
screen.onkeypress(go_right2, 'd')
screen.listen()

score_value = 0
score2_value = 0
