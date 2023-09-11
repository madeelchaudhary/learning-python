from collections import deque

queue = deque(["Eric", "John", "Michael"])
print(queue)

queue.append("Terry")
print(queue)

queue.append("Graham")
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)

if not queue:
    print("No more people to serve")
