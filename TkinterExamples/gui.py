'''https://www.tutorialspoint.com/python3/python_gui_programming.htm'''

from tkinter import *  # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import messagebox
import tkinter

# creating a window
wnd = Tk()
# top.geometry("600x400")

# frame infrastructure for widgets placing
leftMainFrame = Frame(wnd)
leftMainFrame.pack(side=LEFT)
centerMainFrame = Frame(wnd)  # as an example, contents will be packed as grid (look at checkbuttons parent frames)
centerMainFrame.pack(side=LEFT) # unless we set the side param left or right , frames int the top frame will be placed vertically
rightMainFrame = Frame(wnd)
rightMainFrame.pack()


LeftUpperChildFrame = Frame(leftMainFrame)  #child frame of the leftMainFrame
LeftUpperChildFrame.pack(side=TOP)
LeftBottomChildFrame = Frame(leftMainFrame)  #child frame of the leftMainFrame
LeftBottomChildFrame.pack(side=BOTTOM)
RightUpperChildFrame = Frame(rightMainFrame)  #child frame of the rightMainFrame
RightUpperChildFrame.pack(side=TOP)
RightBottomChildFrame = Frame(rightMainFrame)  #child frame of the rightMainFrame
RightBottomChildFrame.pack(side=BOTTOM)




# adding button to the LeftUpperChildFrame and LeftBottomChildFrame in the leftMainFrame
def ButtonCallBack(num):
    msg = messagebox.showinfo("Button"+str(num), "Button" + str(num) + " Pressed")

def ButtonXCallBack():
    msg = messagebox.showinfo("Button", "Button Pressed")

Button1 = Button(LeftUpperChildFrame, text="BUT1", fg="red", command=lambda: ButtonCallBack(1))
Button1.pack(side=LEFT, fill=X)
# Button1.place(x=120, y=80)
Button2 = Button(LeftUpperChildFrame, text="BUT2", fg="blue", command=lambda: ButtonCallBack(2))
Button2.pack(fill=X)
# Button2.place(x=120, y=80)
Button3 = Button(LeftBottomChildFrame, text="BUT3", fg="green", command=lambda: ButtonCallBack(3))
Button3.pack(side=LEFT, fill=X)
# Button3.place(x=120, y=80)
Button4 = Button(LeftBottomChildFrame, text="BUT4", fg="purple", command=ButtonXCallBack)
Button4.pack(fill=X)
# Button4.place(x=120, y=80)



'''
# adding checkbox----------------------------------------------------
class TestTkClass:
    def __init__(self, title, container):
        self.var = IntVar()
        cb = Checkbutton(container, text=title, variable=self.var, onvalue=1, offvalue=0, height=5, width=20, command=self.cbf)
        cb.place(x=200, y=200)
        cb.pack()

    def cbf(self):
        # print("variable is", self.var.get())
        msg = messagebox.showinfo("variable is", str(self.var.get()))

a = TestTkClass(title="option1", centerMainFrame)

'''
def CheckButton1CallBack():
        msg = messagebox.showinfo("Hello Python", "selection!")
        # msg = messagebox.showinfo("Hello Python", "not selected")


CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(centerMainFrame, text="python2", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20, command=CheckButton1CallBack)
C2 = Checkbutton(centerMainFrame, text="python3", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20, command=CheckButton1CallBack)
C1.grid(row=0, column=1)
C2.grid(row=1, column=1)







# adding label----------------------------------------------------
theLabel = Label(RightUpperChildFrame, text="CANVAS SHAPES", fg="white", bg="red")
theLabel.pack(side=TOP, fill=X)  # on fill param, X  means horizontal stretch the widget
check1Label = Label(centerMainFrame, text="OPT1", fg="white", bg="blue")
check1Label.grid(row=0, column=0)
check2Label = Label(centerMainFrame, text="OPT2", fg="white", bg="blue")
check2Label.grid(row=1, column=0)

# adding canvas shapes----------------------------------------------------
C = Canvas(RightBottomChildFrame, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
line = C.create_line(50, 50, 150, 100, fill='white')
# image1 = C.create_bitmap()
C.pack(side=BOTTOM)








wnd.mainloop()






