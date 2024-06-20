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
