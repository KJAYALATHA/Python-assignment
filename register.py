product_name=input("enter a product name")
product_price=int(input("enter a product price"))
product_quantity=int(input("enter a product quantity"))
f=open("admin.txt","r+")
for i in f:
    if (i.split(" ")[0]==product_name):
        print("already added")
        break
else:
    f.write(product_name)
    f.write(" ")
    f.write(str(product_price))
    f.write(" ")
    f.write(str(product_quantity))
    f.write(" ")
    f.write("\n")
    print("item is added")
f.close()
