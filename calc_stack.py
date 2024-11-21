from collections import deque
a = input("").split()
stack = deque()
for i in a:
    stack.append(int(i))
print(list(stack))
while stack:
    elemento = stack.pop()
    print(elemento * 2)