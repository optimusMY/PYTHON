from tkinter import *  # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import messagebox
import tkinter

# creating a window
wnd = Tk()
wnd.geometry("300x100")

label_1 = Label(wnd, text="Name")
label_2 = Label(wnd, text="Password")

entry_1 = Entry(wnd)
entry_2 = Entry(wnd)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

'''CLASSIC WAY TO ADD AN ACTION TO BUTTON AND CHECKBUTTON USING COMMAND PARAM

def ChkBtn_CallBack():
    msg = messagebox.showinfo("Welcome", "You will be kept logged in!")

checkButton1 = Checkbutton(wnd, text="Keep me logged in", command=ChkBtn_CallBack)
checkButton1.grid(columnspan=2)



def But_RegisterCallBack():
    msg = messagebox.showinfo("Welcome", "Registry Successful")


But_register = Button(wnd, text="Register", command=But_RegisterCallBack)
But_register.grid(columnspan=3)
'''

'''NOW WE CAN USE EVENT BINDING WAY TO ADD AN ACTION TO BUTTON AND THE OTHER WIDGETS
EVENT IS USEFUL WHEN YOU BIND A WIDGET TO IT
'''

def ChkBtn_CallBack(event):
    msg = messagebox.showinfo("Welcome", "You will be kept logged in!")

checkButton1 = Checkbutton(wnd, text="Keep me logged in")
checkButton1.bind("<Button-2>", ChkBtn_CallBack)  # designated to wheelbuttonclick event
checkButton1.grid(row=2, columnspan=2)


def But_LoginCallBack():
    msg = messagebox.showinfo("Welcome", "Login Successful")


But_login = Button(wnd, text="  Login  ", command=But_LoginCallBack)
But_login.grid(row=3, column=0)




def But_RegisterCallBack(event):
    msg = messagebox.showinfo("Welcome", "Registry Successful")


But_register = Button(wnd, text="Register")
But_register.bind("<Button-1>", But_RegisterCallBack)  # designated to leftclick event
But_register.grid(row=3, column=1)



But_passMiss = Button(wnd, text="Pass Miss", command=wnd.quit)
But_passMiss.grid(row=3, column=2)

wnd.mainloop()







