l=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    l.append(element)
    max1=len(l[0])
    temp=l[0]
for i in l:
    if(len(i)>max1):
       max1=len(i)
       temp=i
print("Longest Word:",temp)
print("Length of longest word :",max1)
