n=int(input("Enter the limit:"))
print("\nEnter some numbers:")
lst=[]
for i in range (0,n):
 lst.append(int(input()))
squared_numbers = [number ** 2 for number in lst]
print("Square of numbers:",squared_numbers)