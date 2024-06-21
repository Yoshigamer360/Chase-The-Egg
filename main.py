# Hungry turtle
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
player2.color('purple')
player2.penup()
player2.setheading(180)

killer = turtle.Turtle()
killer.shape('square')
killer.color('white')
killer.penup()
killer.setheading(90)
killer.goto(215, -220)


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

obstacle_5 = turtle.Turtle()
obstacle_5.shape('square')
obstacle_5.color('white')
obstacle_5.penup()
obstacle_5.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))

obstacle_6 = turtle.Turtle()
obstacle_6.shape('square')
obstacle_6.color('white')
obstacle_6.penup()
obstacle_6.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))

obstacle_7 = turtle.Turtle()
obstacle_7.shape('square')
obstacle_7.color('white')
obstacle_7.penup()
obstacle_7.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(10, 240))

obstacle_8 = turtle.Turtle()
obstacle_8.shape('square')
obstacle_8.color('white')
obstacle_8.penup()
obstacle_8.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(10, 240))


# Create the food turtle
food = turtle.Turtle()
food.shape('circle')
food.color('blue')
food.penup()
food.goto(random.randint((-width/2)+10, (width/2)-10),
          random.randint((-height/2)+10, (height/2)-10))

food2 = turtle.Turtle()
food2.shape('circle')
food2.color('purple')
food2.penup()
food2.goto(random.randint((-width/2)+10, (width/2)-10),
           random.randint((-height/2)+10, (height/2)-10))

# Create the score turtle
score = turtle.Turtle()
score.shape('circle')
score.color('white')
score.hideturtle()
score.penup()
score.goto((-width/2)+10, (height/2)-30)
score.write('Player 1s score is 0', align='left', font=('Courier', 18, 'normal'))

score2 = turtle.Turtle()
score2.shape('circle')
score2.color('white')
score2.hideturtle()
score2.penup()
score2.goto((-width/2)+10, (height/2)-495)
score2.write('Player 2s score is 0', align='left', font=('Courier', 18, 'normal'))

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
    player.forward(6)
    player2.forward(6)
    killer.forward(2)
    
    
    
    # Check for collisions with food
    if player.distance(food) < 20:
        food.goto(random.randint((-width/2)+10, (width/2)-10),
                  random.randint((-height/2)+10, (height/2)-10))
        score_value += 10
        score.clear()
        score.write(f'Player 1: {score_value}', align='left', font=('Courier', 18, 'normal'))

    elif player.distance(killer) < 20:
        player.goto(0,0)
        score_value -= 30
        score.clear()
        score.write(f'Player 1: {score_value}', align='left', font=('Courier', 18, 'normal'))    
    elif player.distance(obstacle_1) < 20:
        player.goto(0,0)
        obstacle_1.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(10, 240))
        score_value -= 30
        score.clear()
        score.write(f'Player 1: {score_value}', align='left', font=('Courier', 18, 'normal'))
    elif player.distance(obstacle_2) < 20:
        player.goto(0,0)
        obstacle_2.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(10, 240))
        score_value -= 30
        score.clear()
        score.write(f'Player 1: {score_value}', align='left', font=('Courier', 18, 'normal'))
    elif player.distance(obstacle_3) < 20:
        player.goto(0,0)
        obstacle_3.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score_value -= 30
        score.clear()
        score.write(f'Player 1: {score_value}', align='left', font=('Courier', 18, 'normal'))
    elif player.distance(obstacle_4) < 20:
        player.goto(0,0)
        obstacle_4.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score_value -= 30
        score.clear()
        score.write(f'Player 1: {score_value}', align='left', font=('Courier', 18, 'normal'))
    elif player.distance(obstacle_5) < 20:
        player.goto(0,0)
        obstacle_5.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score_value -= 30
        score.clear()
        score.write(f'Player 1: {score_value}', align='left', font=('Courier', 18, 'normal'))
    elif player.distance(obstacle_6) < 20:
        player.goto(0,0)
        obstacle_6.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score_value -= 30
        score.clear()
        score.write(f'Player 1: {score_value}', align='left', font=('Courier', 18, 'normal'))
    elif player.distance(obstacle_7) < 20:
        player.goto(0,0)
        obstacle_7.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(10, 240))
        score_value -= 30
        score.clear()
        score.write(f'Player 1: {score_value}', align='left', font=('Courier', 18, 'normal'))
    elif player.distance(obstacle_8) < 20:
        player.goto(0,0)
        obstacle_8.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(10, 240))
        score_value -= 30
        score.clear()
        score.write(f'Player 1: {score_value}', align='left', font=('Courier', 18, 'normal'))

        



    if player2.distance(food2) < 20:
        food2.goto(random.randint((-width/2)+10, (width/2)-10),
                  random.randint((-height/2)+10, (height/2)-10))
        score2_value += 10
        score2.clear()
        score2.write(f'Player 2: {score2_value}', align='left', font=('Courier', 18, 'normal'))

    elif player2.distance(killer) < 20:
        player.goto(0,0)
        score2_value -= 30
        score2.clear()
        score2.write(f'Player 2: {score2_value}', align='left', font=('Courier', 18, 'normal'))
    elif player2.distance(obstacle_1) < 20:
        player.goto(0,0)
        obstacle_1.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(10, 240))
        score2_value -= 30
        score2.clear()
        score2.write(f'Player 2: {score2_value}', align='left', font=('Courier', 18, 'normal'))
    elif player2.distance(obstacle_2) < 20:
        player.goto(0,0)
        obstacle_2.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(10, 240))
        score2_value -= 30
        score2.clear()
        score2.write(f'Player 2: {score2_value}', align='left', font=('Courier', 18, 'normal'))
    elif player2.distance(obstacle_3) < 20 :
        player.goto(0,0)
        obstacle_3.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score2_value -= 30
        score2.clear()
        score2.write(f'Player 2: {score2_value}', align='left', font=('Courier', 18, 'normal'))
    elif player2.distance(obstacle_4) < 20:
        player.goto(0,0)
        obstacle_4.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score2_value -= 30
        score2.clear()
        score2.write(f'Player 2: {score2_value}', align='left', font=('Courier', 18, 'normal'))
    elif player2.distance(obstacle_5) < 20:
        player.goto(0,0)
        obstacle_5.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score2_value -= 30
        score2.clear()
        score2.write(f'Player 2: {score2_value}', align='left', font=('Courier', 18, 'normal'))
    elif player2.distance(obstacle_6) < 20:
        player.goto(0,0)
        obstacle_6.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(-240, -10))
        score2_value -= 30
        score2.clear()
        score2.write(f'Player 2: {score2_value}', align='left', font=('Courier', 18, 'normal'))
    elif player2.distance(obstacle_7) < 20:
        player.goto(0,0)
        obstacle_7.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(10, 240))
        score2_value -= 30
        score2.clear()
        score2.write(f'Player 2: {score2_value}', align='left', font=('Courier', 18, 'normal'))
    elif player2.distance(obstacle_8) < 20:
        player.goto(0,0)
        obstacle_8.goto(random.randint((-width/2)+10, (width/2)-10),
                random.randint(10, 240))
        score2_value -= 30
        score2.clear()
        score2.write(f'Player 2: {score2_value}', align='left', font=('Courier', 18, 'normal'))

    if food.distance(obstacle_1) < 30 or food.distance(obstacle_2) < 30 or food.distance(obstacle_8) < 30 or food.distance(obstacle_3) < 30 or food.distance(obstacle_4) < 30 or food.distance(obstacle_5) < 30 or food.distance(obstacle_6) < 30 or food.distance(obstacle_7) < 30:
        food.goto(random.randint((-width/2)+10, (width/2)-10),
                  random.randint((-height/2)+10, (height/2)-10))
    if food2.distance(obstacle_1) < 30 or food.distance(obstacle_2) < 30 or food.distance(obstacle_8) < 30 or food.distance(obstacle_3) < 30 or food.distance(obstacle_4) < 30 or food.distance(obstacle_5) < 30 or food.distance(obstacle_6) < 30 or food.distance(obstacle_7) < 30:
        food2.goto(random.randint((-width/2)+10, (width/2)-10),
                   random.randint((-height/2)+10, (height/2)-10))

    if score_value > 299:
        score.clear()
        score.write(f'Player 1 wins', font=('Courier', 18, 'normal'))
        score2.clear()
        score2.write(f'You lose', font=('Courier', 18, 'normal'))
        turtle.done()
    elif score2_value > 299:
        score2.clear()
        score2.write(f'Player 2 wins', font=('Courier', 18, 'normal'))
        score.clear()
        score.write(f'You lose', font=('Courier', 18, 'normal'))
        turtle.done()
        
    
    # Check for collisions with the walls
    x, y= player.position()
    if abs(x) > (width/2) or abs(y) > (height/2): player.goto(0,0)

    x, y= player2.position()
    if abs(x) > (width/2) or abs(y) > (height/2): player2.goto(0,0)

    x, y= killer.position()
    if abs(x) > (width/2) or abs(y) > (height/2): killer.goto(215, -220)
