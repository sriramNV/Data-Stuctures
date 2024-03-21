# Lists in python are like arrays, an ordered collection of items/data.
# items/data in Lists dont need to be of same type
# the elements in list can be accessed via the assgned index
# The starting index is always 0 for the list and N-1 for the last element if there are N elements in list

# list declaration
List = [1, 2, 3, "4", "555", 3, "B", "B", 6.7]
List1 = []  # empty list declaration
List2 = [4, 5, 6, 2, 3, 1, 8, 33, 21, 45, 22, 98, 123, 226, 90, 9]
print("List: ", List)


# Basic List operations
# -------------------------------------------------------------------------------------------------------------------------------------------

# 1. Append:- append(x) function adds an element 'x' to the end of list

List.append("B")
List.append(6)
print("List after appending B and 6: ", List)
# -------------------------------------------------------------------------------------------------------------------------------------------

# 2. Extend:- extend(iterable) function adds another list of elements/iterables to the end of a list

List1.extend(List)
print("List1 after extending List on List1: ", List1)
# -------------------------------------------------------------------------------------------------------------------------------------------

# 3. Inser:- insert(i, x) function inserts an element 'x' to the index i to the list

List1.insert(2, "C")  # inserts element 'C' to the index 2 of the list List1
print("List1 after inserting C on index 2: ", List1)

List1.insert(len(List1), "D")  # inserts element 'D' to the end  of the list List1
print("List1 after inserting D at end : ", List1)

List1.insert(0, "A")  # inserts element 'A' to the beginning of the list List1
print("List1 after inserting A at beginning: ", List1)
# -------------------------------------------------------------------------------------------------------------------------------------------

# 4. Remove:- remove(x) function removes the first element 'x' in the list

List1.remove(3)  # removes first element 3 from the list
print("List1 after removing first 3: ", List1)
# -------------------------------------------------------------------------------------------------------------------------------------------

# 5. Pop:- pop([i]) function pops the element at position i in the list, if no index is given it removes the last item from the list and returns the element

List1.pop(5)  # poping element at postion 5
print("List1 after popping the element at index 5: ", List1)

List1.pop()  # popping last element in the list
print("List1 after popping : ", List1)

ele = List1.pop(
    2
)  # the element at position 2 will be popped from list List1 and the value will be returned to ele
print("List1 after popping the element at index 2: ", List1)
print("ele", ele)
# -------------------------------------------------------------------------------------------------------------------------------------------

# 6. Clear:- clear() function clears/removes all the elements from the list
List.clear()
print("List after clearing it: ", List)
# -------------------------------------------------------------------------------------------------------------------------------------------

# 7. Index:- index(x) function returns the index of first element of value x
indx = List1.index("C")
print("Index of C: ", indx)
# -------------------------------------------------------------------------------------------------------------------------------------------

# 8. Count:- count(x) function returns the number of times the element x occurs in the list
countB = List1.count("B")
print("List1: ", List1)
print("count of B", countB)
# -------------------------------------------------------------------------------------------------------------------------------------------

# 9. Sort:- sort(*, key = None, reverse = False) function sorts the given list, the elements in the list needs to be of same type
List2.sort()
print("List1 after sort: ", List2)
# -------------------------------------------------------------------------------------------------------------------------------------------

# 10. Reverse:- reverse() function reverses the given list
List1.reverse()
print("List1 after reverse: ", List1)
# -------------------------------------------------------------------------------------------------------------------------------------------

# 11. Copy:- copy() function runs shallow copy of the list

List = List1.copy()
print("List after copying List1 to it: ", List)
# -------------------------------------------------------------------------------------------------------------------------------------------

# 12.Del:- del statement can delete the element from list, it uses index to delete the element and we can use slicings to remove from list

del List1[2:5]  # deleting the elements from index 2-5(from 2 to 4)
print("List1 after deleting the elements from index 2 to 4: ", List1)
