import turtle
import winsound
import random

class Player:
    'Common base class for all Players'
    playerCount = 0

    def __init__(self, PName, Pscore):
        self.Name = PName
        self.Score = Pscore
        Player.playerCount += 1

    def displayCount(self):
        print("Total Players %d" % Player.playerCount)

    def displayPlayer(self):
        print("Player_Name : ", self.Name, ", Player_Points: ", self.Score)

'''
pname = input("Player1 Name? ")
ppoints = input("Player1 Points? ")
p1 = Player(pname, ppoints)
pname = input("Player2 Name? ")
ppoints = input("Player2 Points? ")
p2 = Player(pname, ppoints)
'''
p1 = Player("Player1", 0)
p2 = Player("Player2", 0)






# WINDOW SETUP----------------------------------------------------------------------------------------------
wnd = turtle.Screen()
wnd.title(" PONG GAME ")
wnd.bgcolor("darkgreen")
wnd.setup(width=800, height=600)
''' ekran merkezi (0,0) noktasi yani en sag (400,0)  ensol (-400,0)  en üst (0,300)  enalt (0,-300) noktalaridir'''
wnd.tracer(0)


# center circle
circ1 = turtle.Turtle()
circ1.speed(0)
circ1.shape("circle")
circ1.color("white")
circ1.shapesize(stretch_wid=8, stretch_len=8)
circ1.penup()
circ1.goto(0, 0)
# center circle
circ2 = turtle.Turtle()
circ2.speed(0)
circ2.shape("circle")
circ2.color("darkgreen")
circ2.shapesize(stretch_wid=7.5, stretch_len=7.5)
circ2.penup()
circ2.goto(0, 0)

# center line
cline = turtle.Turtle()
cline.speed(0)
cline.shape("square")
cline.color("white")
cline.shapesize(stretch_wid=50, stretch_len=0.3)
cline.penup()
cline.goto(0, 0)


# Paddle A
padA = turtle.Turtle()
padA.speed(0)
padA.shape("square")
padA.color("blue")
padA.shapesize(stretch_wid=6, stretch_len=1)
padA.penup()
padA.goto(-350, 0)


# Paddle B
padB = turtle.Turtle()
padB.speed(0)
padB.shape("square")
padB.color("blue")
padB.shapesize(stretch_wid=6, stretch_len=1)
padB.penup()
padB.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
# ball.shapesize(stretch_wid=1, stretch_len=1)  # you can scale the ball size
ball.penup()
ball.goto(0, 0)
# stepxy = float(random.randint(-5, 5))*0.2
# the sign designated by (-1 ** random.randint(1, 2)) term which varies randomly -1 or 1
direction = -1 ** random.randint(0, 2)     # random.randint(0, 2)
ball.dx = 0.3 * direction   # ball moves on x axis 0.3 per step
ball.dy = 0.3 * direction   # ball moves on y axis 2 pixels per step



# scoreboard setup
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-50, wnd.window_height()/2 - 40)
pen.write(p1.Name + ":" + str(p1.Score) + \
          "                         " + p2.Name + ":" + str(p2.Score) \
          , align="center", font=("Courier", 18, "normal"))


# FUNCTIONS

# update scores of players on the scoreboard
def RefreshScore():
    pen.clear()
    pen.write(p1.Name + ":" + str(p1.Score) + \
              "                         " + p2.Name + ":" + str(p2.Score) \
              , align="center", font=("Courier", 18, "normal"))


# paddleA moves up
def paddleA_up():
    y = padA.ycor()
    y += 60
    padA.sety(y)

# paddleA moves down
def paddleA_down():
    y = padA.ycor()
    y -= 60
    padA.sety(y)

# paddleB moves up
def paddleB_up():
    y = padB.ycor()
    y += 60
    padB.sety(y)

# paddleB moves down
def paddleB_down():
    y = padB.ycor()
    y -= 60
    padB.sety(y)


def moveball():
    # ball.setx(ball.xcor() + ball.dx)
    # ball.sety(ball.ycor() + ball.dy)
    ball.goto(ball.xcor() + ball.dx, ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > (wnd.window_height() / 2 - 10):
        ball.sety(wnd.window_height() / 2 - 10)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.ycor() < -1 * (wnd.window_height() / 2 - 10):
        ball.sety(-1 * (wnd.window_height() / 2 - 10))
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > (wnd.window_width() / 2 - 10):  # if ball goes beyond padB
        # ball.setx(wnd.window_width()/2 - 10)
        ball.goto(0, 0)
        ball.dx *= -1
        p1.Score += 1
        RefreshScore()
        winsound.PlaySound("shotgun.wav", winsound.SND_ASYNC)


    elif ball.xcor() < -1 * (wnd.window_width() / 2 - 10):  # if ball goes beyond padA
        # ball.setx(-1*(wnd.window_width()/2 - 10))
        ball.goto(0, 0)
        ball.dx *= -1
        p2.Score += 1
        RefreshScore()
        winsound.PlaySound("shotgun.wav", winsound.SND_ASYNC)

    # paddle and ball collision
    elif (ball.xcor() < padA.xcor() + 10) and (ball.ycor() < (padA.ycor() + 60)) and (ball.ycor() > (padA.ycor() - 60)):
        ball.setx(padA.xcor() + 10)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif (ball.xcor() > padB.xcor() - 10) and (ball.ycor() < (padB.ycor() + 60)) and (ball.ycor() > (padB.ycor() - 60)):
        ball.setx(padB.xcor() - 10)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


# keyboard event binding
wnd.listen()
wnd.onkeypress(paddleA_up, "w")
wnd.onkeypress(paddleA_down, "s")
wnd.onkeypress(paddleB_up, "Up")
wnd.onkeypress(paddleB_down, "Down")


