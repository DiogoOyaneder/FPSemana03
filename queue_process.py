from collections import deque

a = input("").split()
queue = deque()
for i in a:
    queue.appendleft(i)
print(list(queue))
for i in queue:
    if 'a' in i:
        print(i)
