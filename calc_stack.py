from collections import deque

a = input("").split()
stack = deque()
for i in a:
    stack.append(int(i))
print(stack)
while stack:
    n = stack.pop()
    print(n * 2)