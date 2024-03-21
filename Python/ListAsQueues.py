# Queue is a data structure which follows FIFO order
# FIFO implied that the first element which is added to the queue is removed fcom the queue first

# List is not efficient for Queue DS as
#   even if appends and pop at end of list are fast,
#   doing the same from beginning of list is slow as all the elements needs to be shifted one by one
# To implement queue, we use collections.deque which is designed to have fast appends and pops from both end
# In queue the element is appended at last of list and removed from beginning of the list


from collections import deque

queue = deque([1, 2, 3, 4, 5, 6, 7, 8])  # using deque for declaring queue
print("Queue: ", queue)

queue.append(9)  # appending 9 to the queue
print("appended 9 to Queue: ", queue)
queue.append(10)  # appending 10 to the queue
print("appended 10 to Queue: ", queue)
print("Queue: ", queue)

ele = queue.popleft()  # removing element from the queue
print("Element popped from queue: ", ele)
print("Queue: ", queue)

ele = queue.popleft()  # removing element from the queue
print("Element popped from queue: ", ele)
print("Queue: ", queue)
