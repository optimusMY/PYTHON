from tkinter import *

import time

from PIL import Image

root = Tk()
root.title("BOUNCE GAME")
root.resizable(0, 0)  # neither x nor y axis can be resized
root.wm_attributes("-topmost", 1)

'''
photo = PhotoImage(file="starfield.png")
labelForPhoto = Label(root, image=photo)
labelForPhoto.place(x=0, y=0)
'''

canvas = Canvas(root, width=600, height=500, bd=0, highlightthickness=0)
canvas.pack()

photo = PhotoImage(file="starfield.png")
canvas.create_image(0, 0, image=photo, anchor=NW)

root.update()

SPEED = 2  # step per update ball position  [pixels]

class Ball:
    def __init__(self, canvasinit, colorinit, Paddle):
        self.canvas = canvasinit
        self.color = colorinit
        self.paddle = Paddle
        self.x = 1*SPEED
        self.y = -1*SPEED
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.id = canvas.create_oval(10, 10, 25, 25, fill=colorinit)
        self.canvas.move(self.id, 245, 100)
        self.hittobottomflag = False
        self.scoreboard = self.canvas.create_text(350, 20, text="Score:", font="none 18 bold", fill="red")
        self.score = 0


    def hittopaddle(self, ballpos):
        paddlePos = self.canvas.coords(self.paddle.id)
        # if x2 coord of ballpos exceeds x1 coord of paddle pos, then
        if ballpos[2] >= paddlePos[0] and ballpos[0] <= paddlePos[2]:
            if ballpos[3] >= paddlePos[1] and ballpos[3] <= paddlePos[3]:
                return True

        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)  # deltaX is 0 deltaY is -1 so moves up
        pos = self.canvas.coords(self.id)  # pos will be a list like this [x1, y1, x2, y2]
        if pos[1] <= 0:  # if ball reaches 0 on y axis then balldirectiony will be down
            self.y = 1*SPEED
        if pos[3] >= self.canvas_height:  # if ball reaches canvas_height on y axis then balldirectiony will be up
            self.y = -1*SPEED
            self.hittobottomflag = True
        if pos[0] <= 0:  # if ball reaches 0 on x axis then balldirectionx will be right
            self.x = 1*SPEED
        if pos[2] >= self.canvas_width:  # if ball reaches self.canvas_width on x axis then balldirectionx will be left
            self.x = -1*SPEED
        if self.hittopaddle(pos) == True:
            self.y = -1*SPEED
            self.score += 10
            self.canvas.itemconfig(self.scoreboard, text="Score:{}".format(self.score))





class Paddle:
    def __init__(self, canvasinit, colorinit):
        self.canvas = canvasinit
        self.color = colorinit
        self.id = canvas.create_rectangle(0, 350, 100, 360, fill=colorinit)
        self.canvas.move(self.id, 245, 100)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.moveleft)
        self.canvas.bind_all('<KeyPress-Right>', self.moveright)


    def draw(self):
        self.canvas.move(self.id, self.x, 0)  #moving rectangle self.x as deltaX
        pos = self.canvas.coords(self.id)

        if pos[0] < 0:  # if paddle reaches 0 on x axis then paddledirectionx will be 0
            self.x = 0  #stop x movement
        if pos[2] > self.canvas_width:  # if paddle reaches canvas_width on x axis then paddledirectionx will be 0
            self.x = 0  #stop x movement


    def moveright(self, evt):
        self.x = 1*SPEED
    def moveleft(self, evt):
        self.x = -1*SPEED


bluepaddle = Paddle(canvas, 'blue')
ball = Ball(canvas, 'red', bluepaddle)

onceFlag = False

while 1:
    if ball.hittobottomflag == False:
        ball.draw()
        bluepaddle.draw()
    elif onceFlag == False:  # in order to apply this block for one time we are checking the onceFlag
        canvas.create_text(300, 100, text="Game Over :(", font="none 18 bold", fill="red")
        onceFlag = True

    root.update_idletasks()
    root.update()
    time.sleep(0.01)


