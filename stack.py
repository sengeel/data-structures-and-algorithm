stack = []
stack.append("welcome")
stack.append("to")
stack.append("great learning")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

from collections import deque
stack = deque()
stack.append("x")
print(stack)
stack.append("y")
stack.append("z")
print(stack)
print(stack.pop())
print(stack)


from queue import LifoQueue

stack = LifoQueue(maxsize=3)
stack.put(2)
stack.put(3)
stack.put(4)
print(stack.qsize())
print(stack.full())
stack.get()
print(stack.full())
