# Created by: Yoshi

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
player.penup()

player2 = turtle.Turtle()
player2.shape('turtle')
player2.color('blue')
player2.penup()
player2.setheading(180)

# Create obstacle turtle
obstacle_1 = turtle.Turtle()
obstacle_1.shape('square')
obstacle_1.color('white')
obstacle_1.penup()
obstacle_1.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))

obstacle_2 = turtle.Turtle()
obstacle_2.shape('square')
obstacle_2.color('white')
obstacle_2.penup()
obstacle_2.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(10, 240))

obstacle_3 = turtle.Turtle()
obstacle_3.shape('square')
obstacle_3.color('white')
obstacle_3.penup()
obstacle_3.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(10, 240))

obstacle_4 = turtle.Turtle()
obstacle_4.shape('square')
obstacle_4.color('white')
obstacle_4.penup()
obstacle_4.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))


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

# Game play loop
while True:
    player.forward(3)
    player2.forward(3)
    
    # Check for collisions with food
    if player.distance(food) < 20:
        food.goto(random.randint((-width/2)+10, (width/2)-10),
                  random.randint((-height/2)+10, (height/2)-10))
        score_value += 10
        score.clear()
        score.write(f'Score: {score_value}', align='left', font=('Courier', 18, 'normal'))
        
    elif player.distance(obstacle_1) < 20:
        player.goto(0,0)
        obstacle_1.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score_value -= 30
        score.clear()
        score.write(f'Score: {score_value}', align='left', font=('Courier', 18, 'normal'))
    elif player.distance(obstacle_2) < 20:
        player.goto(0,0)
        obstacle_2.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score_value -= 30
        score.clear()
        score.write(f'Score: {score_value}', align='left', font=('Courier', 18, 'normal'))
    elif player.distance(obstacle_3) < 20:
        player.goto(0,0)
        obstacle_3.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score_value -= 30
        score.clear()
        score.write(f'Score: {score_value}', align='left', font=('Courier', 18, 'normal'))
    elif player.distance(obstacle_4) < 20:
        player.goto(0,0)
        obstacle_4.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score_value -= 30
        score.clear()
        score.write(f'Score: {score_value}', align='left', font=('Courier', 18, 'normal'))

        



    if player2.distance(food) < 20:
        food.goto(random.randint((-width/2)+10, (width/2)-10),
                  random.randint((-height/2)+10, (height/2)-10))
        score2_value += 10
        score2.clear()
        score2.write(f'Score: {score2_value}', align='left', font=('Courier', 18, 'normal'))

    elif player2.distance(obstacle_1) < 20:
        player.goto(0,0)
        score_value -= 30
        obstacle_1.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score.clear()
        score.write(f'Score: {score_value}', align='left', font=('Courier', 18, 'normal'))
    elif player2.distance(obstacle_2) < 20:
        player.goto(0,0)
        score_value -= 30
        obstacle_2.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score.clear()
        score.write(f'Score: {score_value}', align='left', font=('Courier', 18, 'normal'))
    elif player2.distance(obstacle_3) < 20 :
        player.goto(0,0)
        obstacle_3.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score_value -= 30
        score.clear()
        score.write(f'Score: {score_value}', align='left', font=('Courier', 18, 'normal'))
    elif player2.distance(obstacle_4) < 20:
        player.goto(0,0)
        obstacle_4.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score_value -= 30
        score.clear()
        score.write(f'Score: {score_value}', align='left', font=('Courier', 18, 'normal'))



        
    
    # Check for collisions with the walls
    x, y= player.position()
    if abs(x) > (width/2) or abs(y) > (height/2): player.goto(0,0)

    x, y= player2.position()
    if abs(x) > (width/2) or abs(y) > (height/2): player2.goto(0,0)
