# class Queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, item):
#         self.queue.append(item)

#     def dequeue(self):
#         if len(self.queue) < 1:
#             return None
#         else: 
#             return self.queue.pop(0)

#     def display(self):
#         print(self.queue)

#     def size(self):
#         return len(self.queue)
    
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# q.display()
# q.dequeue()
# print("After removing an element")
# q.display()

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self): 
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            raise Exception("The queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size+=1

    def dequeue(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        return self.queue[self.front]

    def __str__(self):
        if self.is_empty():
            print("Queue is empty")
        items = []
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            items.append(self.queue[index])
        return f"Queue: {str(items)}"

# Initialize the circular queue with a capacity of 5
cq = CircularQueue(5)

# # Enqueue tasks (represented by integers)
# tasks = [10, 20, 30, 40, 50]
# for task in tasks:
#     cq.enqueue(task)

# print(cq)  # Output: Queue: 10 20 30 40 50

# # Process and dequeue tasks
# while not cq.is_empty():
#     task = cq.dequeue()
#     # Perform some calculations with the task
#     result = task * 2  # Example calculation: doubling the task value
#     print(f"Processed task {task}, result: {result}")

# print(cq)  # Output: Queue is empty
# # cq.dequeue()
# # print(cq)


cq.enqueue("Banana")
cq.enqueue(3)
cq.enqueue("orange")
print(cq)
cq.dequeue()
print(cq)
cq.enqueue("Rect")
print(cq)
