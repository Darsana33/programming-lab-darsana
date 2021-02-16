#Generate Fibonacci series of N terms

a= int(input("Enter the limit : "))
m= 0
n = 1
sum = 0
count = 1
print("Fibonacci Series : ")
while(count <= a):
  print(sum, end = " ")
  count += 1
  m = n
  n = sum
  sum = m + n