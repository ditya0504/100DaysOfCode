import turtle
import random
import time
delay=0.1
score=0
hightestscore=0

#snakebodies
bodies=[]
#getting a screen l canvas
s=turtle.screen ()
s.title("snake Game")
s.bgcolor("gray")
s.setup (width=600,hight=600)
#creat snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)
food.st()
#score board
sb=turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("score:0  l  heighest score:   0")

def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
        if head.direction!="up":
            head.direction"down"
def moveleft():
            if head.direction!="right":
                head.direction="left"
def moveright():
                if head.direction!="left":
                    head.direction="right"
def movestop():
                    if head.direction="stop"
def move():
                      if head.direction=="up":
                          y=head.ycor()
                          head.sety(y+20)
                      if head.direction=="down":
                          y=head.ycor()
                          head.sety(y-20)
                      if head.direction=="left":
                          x=head.xcor()
                          head.setx(x+20)
                      if head.direction=="right":
                          x=head.xcor()
                          head.setx(x+20)
#Event Handling - key mappings
s.listen()
s.onkey(moveup,"up")
s.onkey(movedown,"down")
s.onkey(moveleft,"left")
s.onkey(moveright,"right")
s.onkey(movestop,"space")

#main loop
while True:








