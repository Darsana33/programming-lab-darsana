a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
c=float(input("enter the third number:"))
if(a>b and a>c):
    big=a
elif(b>c and b>a):
    big=b
else:
    big=c
print("Biggest number is:",big)
    