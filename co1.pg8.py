d=str(input("Enter data:"))
for i in range(0,len(d)):
    if i==0:
        print(d[i],end="")
    else:
        if d[i] == d[0]:
            print("$",end="")
        else:
            print(d[i],end="")

