from tkinter import *
from tkinter import messagebox
w=Tk()
w.geometry("200x300")
w.title("search")
w.config(bg="pink")
Label(text="product_name").grid(row=0,column=0)
product_name=Entry()
product_name.grid(row=0,column=1)
Label(text="product_price").grid(row=1,column=0)
product_price=Entry()
product_price.grid(row=1,column=1)
Label(text="product_quantity").grid(row=2,column=0)
product_quantity=Entry()
product_quantity.grid(row=2,column=1)
def search():
    pname=product_name.get()
    f=open("admin.txt","r")
    for i in f:
        if (i.split(" ")[0])==pname:
            messagebox.showinfo("search","product available")
            break
    else:
        messagebox.showinfo("search","product not available")
Button(text="search",command=search).grid(row=3,column=0,columnspan=2)
w.mainloop()




