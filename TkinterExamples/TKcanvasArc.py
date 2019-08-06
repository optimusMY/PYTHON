from tkinter import *

import random


root = Tk()
root.title("Arcs")



'''
ch, cw = 500, 500
c1 = Canvas(root, height=ch, width=cw, bg="black")
c1.create_arc(30, 30, 200, 200, start=30, extent=45, outline="brown", fill="yellow", width=4)
c1.create_arc(10, 130, 200, 230, start=30, extent=145, outline="brown", fill="yellow", width=4)
c1.create_arc(30, 30, 100, 100, start=30, extent=295, outline="green", width=2)
c1.create_arc(50, 50, 65, 60, start=30, extent=310, outline="green", width=2)
c1.pack()



c1.create_arc(30, 30, 200, 200, start = 30, extent = 45, outline = "brown", fill = "yellow", width = 4) 
The coordinates of the first point are (30, 30), and of the last point are (200, 200). 
start is starting angle(ccw positive angle) and extent is angle between 
The attributes of outline_color and width_size go with "outline" and "width", respectively.
'''

'''
canvas = Canvas(root, width=600, height=600)

x1 = 50
y1 = 50
wid = 100
heig = 50
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=0, extent=30, width=2)  # , outline="brown", fill="yellow"

y1 += 50
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=0, extent=60, width=2)  # , outline="brown", fill="yellow"

y1 += 50
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=0, extent=90, width=2)  # , outline="brown", fill="yellow"

y1 += 50
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=0, extent=135, width=2)  # , outline="brown", fill="yellow"

y1 += 50
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=0, extent=180, width=2)  # , outline="brown", fill="yellow"

y1 += 50
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=60, extent=180, width=2)  # , outline="brown", fill="yellow"


canvas.pack()
'''




canvas = Canvas(root, width=600, height=600)

x1 = 50
y1 = 50
wid = 100
heig = 50

canvas.create_arc(x1, y1, x1+wid, y1+heig, start=0, extent=45)  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)

y1 += heig+10
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=0, extent=90)  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)

y1 += heig+10
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=0, extent=135)  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)


y1 += heig+10
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=0, extent=180)  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)

y1 += heig+10
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=0, extent=225)  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)

y1 += heig+10
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=0, extent=270)  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)


y1 += heig+10
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=0, extent=315)  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)

y1 += heig+10
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=0, extent=359)  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)


y1 = 50
x1 += wid+10
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=0, extent=359, width=2, outline="brown", fill="yellow")  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)

y1 += heig+10
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=45, extent=315, width=2, outline="brown", fill="yellow")  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)


y1 += heig+10
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=90, extent=270, width=2, outline="brown", fill="yellow")  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)

y1 += heig+10
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=135, extent=225, width=2, outline="brown", fill="yellow")  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)

y1 += heig+10
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=180, extent=180, width=2, outline="brown", fill="yellow")  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)

y1 += heig+10
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=225, extent=135, width=2, outline="brown", fill="yellow")  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)

y1 += heig+10
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=270, extent=90, width=2, outline="brown", fill="yellow")  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)

y1 += heig+10
canvas.create_arc(x1, y1, x1+wid, y1+heig, start=315, extent=45, width=2, outline="brown", fill="yellow")  # , width=2, outline="brown", fill="yellow"
canvas.create_rectangle(x1, y1, x1+wid, y1+heig)



canvas.create_text(400, 300, text="HelloCody", font="none 18 bold", fill="magenta")


canvas.pack()








xpos = 0
ypos = 0

def leftmove(event):
    global ypos
    global xpos
    if xpos > 0:
        xpos -= 10
        labelx.configure(text=str(xpos))



def rightmove(event):
    global ypos
    global xpos
    if xpos < 300:
        xpos += 10
        labelx.configure(text=str(xpos))


def upmove(event):
    global ypos
    global xpos
    if ypos > 0:
        ypos -= 10
        labely.configure(text=str(ypos))



def downmove(event):
    global ypos
    global xpos
    if ypos < 300:
        ypos += 10
        labely.configure(text=str(ypos))



labelx = Label(root, bg='red', fg='white', font="none 16 bold")
labelx.pack(side=LEFT, padx=10)
labely = Label(root, bg='red', fg='white', font="none 16 bold")
labely.pack(side=LEFT, padx=2)

root.bind("<Left>", leftmove)
root.bind("<Right>", rightmove)
root.bind("<Up>", upmove)
root.bind("<Down>", downmove)


root.mainloop()


