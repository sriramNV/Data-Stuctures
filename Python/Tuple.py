# Tuple is another sequence data type in Python, it consists of number of elements seperated by commas or in normal brackets ()
# Tuples are immutable
# Tuples contains hetrogeneous typs of elements 


# Tuple declaration
t = 123, 456, 678, 90
print("T: ", t)
print("Type of T: ", type(t))


#Nested Tuple
t = 1, 2, 3, (4, 5, 6,)

#Stings in a tuple are considered to be single element

t = 'hello',  # note the single trailing comma to declare the element as tuple instead of string
print("T: ", t)
print("Type of T: ", type(t))