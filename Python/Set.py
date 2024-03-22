# Set is an unordered collections with no duplicate elements
# Set supports matematical set operation like union, intersection, ...
# Set is declared in curly braces {} or using the function set()

# Set declaration
s = {'banana','apple','orange'}
s1 = set("aaabbbcccdddeee") # this will automatically update the set with unique elements on runtime
s2 = set("Abracadabra")


print("S: ", s)
print("S1: ", s1)
print("S2: ", s2)
print("apple in s? ", ('apple' in s))

# Unique letters in a
print("S1 - S2: ", s1 - s2) 

# letters in a or b or both
print("S1 | S2 ", s1 | s2)

# letters in both a and b
print("S1 & S2 ", s1 & s2)

# letters in both a or b but not in both
print("S1 ^ S2 ", s1 ^ s2)