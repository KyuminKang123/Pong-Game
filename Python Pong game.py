import turtle
#Create 2 sticks, create a line in center, create ball, create score to keep track, create screen


#Create screen

screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(width=1000,height=600)
screen.tracer(0)


#Create stick

leftstick=turtle.Turtle()
leftstick.speed(0)
leftstick.shape("square")
leftstick.color("white")
leftstick.shapesize(stretch_wid=10,stretch_len=1)
leftstick.penup()
leftstick.goto(-400,0)


rightstick=turtle.Turtle()
rightstick.speed(0)
rightstick.shape("square")
rightstick.color("white")
rightstick.shapesize(stretch_wid=10,stretch_len=1)
rightstick.penup()
rightstick.goto(400,0)


#Ball

ball=turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=2

#Score

player1=0
player2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,200)
score.write("0,0",align="center",font=("calibri",12,"normal"))
#Create 2 sticks, create a line in center, create ball, create score to keep track, create screen

#Moving Leftstick

def leftstickmovingup():
    y=leftstick.ycor()
    y+=3
    leftstick.sety(y)
def leftstickmovingdown():
    #ycor allows to find out what the current y coordinate of Leftstick 
    y=leftstick.ycor()
    y-=3
    leftstick.sety(y)

def rightstickmovingup():
    y=rightstick.ycor()
    y+=3
    rightstick.sety(y)
def rightstickmovingdown():
    y=rightstick.ycor()
    y-=3
    rightstick.sety(y)

#Moving with keys
screen.listen()
screen.onkeypress(leftstickmovingup,"w")
screen.onkeypress(leftstickmovingdown,"s")
screen.onkeypress(rightstickmovingup,"Up")
screen.onkeypress(rightstickmovingdown,"Down")

#Main game loop
while True:
    screen.update()
#Moving ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
   
    if ball.ycor()>280:
        ball.sety(280)
        ball.dy *=-1
   
    if ball.ycor()<-280:
        ball.sety(-280)
        ball.dy *=-1         

    if ball.xcor()>380:
        ball.goto(0,0)
        ball.dy *=-1
        player1+=1
        score.clear
        score.write("{},{}".format(player1,player2),align="center",font=("calibri",12,"normal"))

    if ball.xcor()<-380:
        ball.goto(0,0)
        ball.dy *=-1
        player2+=1
        score.clear
        score.write("{},{}".format(player1,player2),align="center",font=("calibri",12,"normal"))
    if leftstick.ycor()>280:
        leftstick.sety(280)
        leftstick.ycor

    #Ball bouncing off stick
    if (ball.xcor()<-360 and ball.xcor()>-370) and (ball.ycor()<leftstick.ycor()+40 and ball.ycor()>leftstick.ycor()-40):
        ball.setx(-360)
        ball.dx *=-1

    if (ball.xcor()>360 and ball.xcor()<370) and (ball.ycor()<rightstick.ycor()+40 and ball.ycor()>rightstick.ycor()-40):
        ball.setx(360)
        ball.dx *=-1
