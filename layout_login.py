from tkinter import *
from tkinter import messagebox
w=Tk()
w.geometry("400x300")
w.title("login")
w.config(bg="pink")
Label(text="username").grid(row=0,column=0)
username=Entry()
username.grid(row=0,column=1)
Label(text="password").grid(row=1,column=0)
password=Entry(show="*")
password.grid(row=1,column=1)
def login():
    uname=username.get()
    pwd=password.get()
    f=open("admin.txt","r")
    print(uname)
    for i in f:
        print(i.split(" ")[0])
        if (i.split(" ")[0])==uname and pwd in i.split(" ")[1]:
            messagebox.showinfo("login","authorized user")
            break
    else:
        messagebox.showinfo("unauthorized user")
Button(text="login",command=login).grid(row=2,column=0,columnspan=2)
w.mainloop()