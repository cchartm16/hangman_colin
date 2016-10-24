#Objective: integrate hangman program with some drawing functions from turtle graphics
from turtle import *
size = 25

def sad_face(size):
    penup()
    left(90)
    forward(size)
    left(90)
    forward(size)

    def eye():
        begin_fill()
        circle(size/8)
        end_fill()

    pendown()
    eye()
    penup()
    back(size*2)

    pendown()
    eye()
    penup()

    forward(size)



    left(90)
    forward(size)

    left(90)
    forward(size/2)

    #expression
    pendown()
    left(90)
    circle(size/2, 180)

    penup()
    right(90)
    forward((3/2)*size)
    right(90)
    forward(size/2)
    right(180)
    pendown()

    #outer-circle
    circle(size*2)





def start_gallows(size):
    penup()
    setpos(size * 10, 0)
    pendown()

def straightline(size):
    left(90)
    forward(size * 10)

def hook(size):
    left(90)
    forward(size)

def no_body(size):
    start_gallows(size)
    straightline(size)
    straightline(size)
    hook(size)

def hangman(size):

    left(90)

    sad_face(size)
    # Reorient turtle
    circle(size * 2, 90)
    right(90)
    body(size)



def arm(size, angle, direction):
    setheading(0)
    if direction == "left":
        left(angle)
    elif direction == "right":
        right(angle)
    else:
        raise ValueError("must be string")

    forward(size)
    back(size)
    setheading(0)


def body(size):
    forward(size*2)
    back(size)
    arm(size*2, 45, "left")
    arm(size*2, 135, "left")
    right(90)
    forward(size)
    arm(size*2, 45, "right")
    arm(size*2, 135, "right")



def main():
    no_body(size)

    penup()
    # Forward 2.5 to have the head JUST TOUCHING the hook
    forward(size * 2.5)
    pendown()
    hangman(size)












main()
print(pos())
input()