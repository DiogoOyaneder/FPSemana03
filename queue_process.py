from collections import deque

a = input("").split()
queue = deque()
for i in a:
    queue.appendleft(i)
print(queue)
for i in range(len(queue)):
    word = queue.pop()
    if 'a' in word:
        print(word)