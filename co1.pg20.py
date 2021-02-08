list=[9,11,20,45,12]
print("The list is:",list)
for i in list:
    if(i%2==0):
        list.remove(i)
print("List after removing even numbers:",list)