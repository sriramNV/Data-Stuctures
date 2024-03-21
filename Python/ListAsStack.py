# Stack is a linear data structure that follows LIFO/FILO order.
# LIFO implies that the element that is inserted last comes out first
# FILO implies that the element that is inserted first comes out last

# List is easier to be used as STACK: the top of stack will be the end of list
# To add an item we can use append() without an index to insert the element at top of stack
# To remove and item we can use pop() without an index to retreive the element at the top of stack

stack = [4, 5, 6]

# inserting two values to the top of stack
stack.append(7)
stack.append(8)

print("Stack: ", stack)

# retreiving/removing the values from the top of stack
topItem = stack.pop()
print("removed top Item: ", topItem)
print("Stack: ", stack)


topItem = stack.pop()
print("removed top Item: ", topItem)
print("Stack: ", stack)
