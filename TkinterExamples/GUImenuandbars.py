
from tkinter import *

from tkinter import messagebox


def testCallBack():
    msg = messagebox.showinfo("test", "ok")




wnd = Tk()
wnd.title('Canvas--Menu--Toolbar--Statusbar--Events---CanvasMovement ')

wnd.geometry("800x600")


# MESSAGEBOX YES NO QUESTION FUNCTION---------------------------------------------------------------------------
def quitBargain():
    responseMsg = messagebox.askquestion("Question1", "Are you really sure you  wanna quit")
    if responseMsg == 'yes':
        responseMsg = messagebox.askquestion("Final Question", "Are you really really sure you wanna quit")
        if responseMsg == 'yes':
            wnd.quit()


mainmenu = Menu(wnd)
wnd.config(menu=mainmenu)
submenu = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New   Ctrl+N", command=testCallBack)
submenu.add_separator()
submenu.add_command(label="Exit   Ctrl+Q", command=quitBargain)

editmenu = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo   Ctrl+Z", command=testCallBack)
editmenu.add_command(label="Redo   Ctrl+Y", command=testCallBack)
editmenu.add_separator()
editmenu.add_command(label="Cut     Ctrl+X", command=testCallBack)
editmenu.add_command(label="Copy    Ctrl+C", command=testCallBack)
editmenu.add_command(label="Paste   Ctrl+V", command=testCallBack)
editmenu.add_command(label="Move    Ctrl+M", command=testCallBack)
editmenu.add_separator()
editmenu.add_command(label="Find      Ctrl+F", command=testCallBack)
editmenu.add_command(label="Replace   Ctrl+R", command=testCallBack)

# ADDING TOOLBAR----------------------------------------------------
toolbar = Frame(wnd, bg="magenta")

insertBut = Button(toolbar, text="InsertImage", command=testCallBack)
insertBut.pack(side=LEFT, padx=2, pady=2)  # padx and pady is how many pixels of space are there between toolbar edges and insertButton
printButton = Button(toolbar, text="Print", command=testCallBack)
printButton.pack(side=LEFT, padx=2, pady=2)
zoomButton = Button(toolbar, text="Zoom", command=testCallBack)
zoomButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ADDING STATUSBAR---------------------------------------------------------------------------------------
# bd=1 is border enabled, relief is how its gonna be appeared(SUNKEN selected), anchor is W means west = LEFT
statusbar = Label(wnd, text="STATUS BAR HERE | Process: Running...", fg="white", bg="blue", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)


# ADDING SHAPES USING CANVAS---------------------------------------------------------------------------------------
canvas = Canvas(wnd, width=200, height=200, bg='gray50')
canvas.pack(side=LEFT)

whiteline1 = canvas.create_line(0, 0, 100, 100, fill='white')  # (x1,y1,x2,y2)
redline1 = canvas.create_line(100, 100, 200, 200, fill='red')  # (x1,y1,x2,y2)
greenline1 = canvas.create_line(200, 0, 100, 100, fill='green')  # (x1,y1,x2,y2)
blueline1 = canvas.create_line(100, 100, 0, 200, fill='blue')  # (x1,y1,x2,y2)
yellowcircle = canvas.create_oval(100, 100, 50, 1, fill='yellow')  # (x1,y1,Ydiameter,Xdiameter, fill with yellow)
magentarectangle = canvas.create_rectangle(10, 60, 40, 120 )  #fill='magenta' rectangle(upperleftcornerX, upperleftcornerY, width, height, fill='magenta')

# canvas.delete(yellowcircle)
# canvas.delete(magentarectangle)
# canvas.delete(ALL)

coeff = 1

def moveRightrectangle(event):
    global coeff
    canvas.move(magentarectangle, 1*coeff, 0)  # move(magentarectangle, Xamount, Yamount)


def moveLeftrectangle(event):
    global coeff
    canvas.move(magentarectangle, -1*coeff, 0)

def moveUprectangle(event):
    global coeff
    canvas.move(magentarectangle, 0, -1*coeff)

def moveDownrectangle(event):
    global coeff
    canvas.move(magentarectangle, 0, 1*coeff)

wnd.bind("<Right>", moveRightrectangle)
wnd.bind("<Left>", moveLeftrectangle)
wnd.bind("<Up>", moveUprectangle)
wnd.bind("<Down>", moveDownrectangle)




photo = PhotoImage(file="google.png")
labelForPhoto = Label(wnd, image=photo)
labelForPhoto.pack(side=LEFT)

# ADDING ENTRY textbox---------------------------------------------------------------------------------------
data1str = StringVar()
def EnterKeypressEventHandler(event):  # evaluation of the text by Enter keypress action
    data1str.set("Ans= " + str(eval(entryCalc.get())))  # evaluate result ,convert into string and save into the data1str StringVar
    # labelAnswer.configure(text="Ans= " + str(eval(entryCalc.get())))



entryCalc = Entry(wnd)
entryCalc.bind("<Return>", EnterKeypressEventHandler)
entryCalc.pack(side=LEFT)


# labelAnswer = Label(text="Ans= ", bg='black', fg='green')
labelAnswer = Label(textvariable=data1str, bg='black', fg='green', font="none 16 bold") # labelAnswer will be refreshed by data1str automatically because of textvariable assignment
labelAnswer.pack(side=LEFT)



# ADDING CheckButtons-------------------------------------------------
def chkBut1Handler():
    msg = messagebox.showinfo("CheckButton1Status", str(CheckVar1.get()))

def chkBut2Handler():
    msg = messagebox.showinfo("CheckButton2Status", str(CheckVar2.get()))


CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(wnd, text="Music", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20, command=chkBut1Handler)
C2 = Checkbutton(wnd, text="Video", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20, command=chkBut2Handler)
C1.pack()
C2.pack()





wnd.mainloop()







'''


import tkinter as tk

from tkinter import messagebox

def click(event):
    if object_id is not None:
        coord = can.coords(object_id)
        width = coord[2] - coord[0]
        height = coord[3] - coord[1]

        can.coords(object_id, event.x, event.y, event.x+width, event.y+height)

def delete():
    msg = messagebox.askyesnocancel('Info', 'Delete canvas ?')
    if msg == True:
       can.delete(tk.ALL)

def create_rectangle():
    global object_id

    object_id = can.create_rectangle(10, 10, 70, 70, fill='white', outline='blue', width=3)


def create_line():
    global object_id

    object_id = can.create_line(200, 200, 100, 100, fill='red', width=5)

def create_circle():
    global object_id

    object_id = can.create_oval(10, 10, 70, 70, fill='orange', outline='blue')

# --- main ---

object_id = None

fenetre = tk.Tk()
fenetre.title('Dessin des objets')
fenetre.resizable(width=False, height=False)
fenetre.geometry('400x200+100+50')
fenetre.configure(bg='light green')

can = tk.Canvas(fenetre, bg='white', height=300, width=300)
can.pack(side=tk.RIGHT)
can.bind("<Button-1>", click)

btn_line = tk.Button(fenetre, text='Line', width=30, command=create_line)
btn_line.pack()

btn_rectangle = tk.Button(fenetre, text='Rectangle', width=30, command=create_rectangle)
btn_rectangle.pack()

btn_circle = tk.Button(fenetre, text='Circle', width=30, command=create_circle)
btn_circle.pack()

btn_delete = tk.Button(fenetre, text='Delete', width=30, command=delete)
btn_delete.pack()

fenetre.mainloop()

'''





