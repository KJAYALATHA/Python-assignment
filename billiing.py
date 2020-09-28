product_name=input("enter the product name")
f=open("admin.txt","r")
for i in f:
    if(i.split(" ")[0]==product_name):
        a=(i.split(" ")[1])
        print(a)
        product_quantity=int(input("enter the product quantity"))
        if(int(i.split(" ")[2])>=product_quantity):
            total_price=product_quantity*int(a)
            print(total_price)
        else:
            print("out of stock")


