stringA = input("Enter the word:")
vowels = "AaEeIiOoUu"
result = set([each for each in stringA if each in vowels])
print("The vlowels present in the string:\n ",result)