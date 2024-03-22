# Dictionaies in python are 'Key-value' pair data structure
# The elements of the data structure is accessed by the immutable key values, it can be strings or numbers
# the keys in dictionary should always be unique
# Dictionary is declared inside curly braces with key and value seperated by colon(:) and elements seperated by commas(,)

# Dictionary declaration
D = {3: "Jack", 1: "Bob", 2: "Pete"}
D1 = {"Jack": 3, "Bob": 1, "Pete": 2}

print(D[1]) # printing the element assosiated with key 1
print(D1["Jack"]) # printing the element assosiated with key Jack

print(list(D)) #printing the keys of the dictionary
print(list(D1)) #printing the keys of the dictionary

print(sorted(D)) #printing sorted dict 
print(sorted(D1))