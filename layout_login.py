from tkinter import *
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
Button(text="login").grid(row=2,column=0,columnspan=2)
w.mainloop()