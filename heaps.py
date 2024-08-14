# There are two types of heap
# ! You can use a built in library called heapify

# ? Min Heap: The root node is the smallest in the tree... You can import min heapify

# ? Max Heap : The rooot node is the biggest in the tree

#  Extract:Heap Pop: O(logn)
#  Insert :Heap push : O(logn) 
#! Heap peek: O(1) : returns the min value in the heap
# * Heap Sort : O(nlogn), space : O(1)


# Build Min Heap (Heapify)
# Time: O(n), Space : O(1)

import heapq

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
heapq.heapify(A)
print(A)

# ?Heap Push(Insert)
# * Time Complexity : O(logn)


heapq.heappush(A, 4)
print(A)

# Heap Pop (Extract Min)
# Time : O(logn)

minn = heapq.heappop(A)


print(A)
print(minn)




# Heap Push Pop : Time : O(logn)
heapq.heappushpop(A, 99)
print(A)

# Peak at Min: Time O(1)
print(A[0])

# Max Heap

B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)

for i in range(n):
  B[i] = -B[i]

heapq.heapify(B)
print()

print(B)

print()
largest = -heapq.heappop(B)


print(largest)



# List to be turned into a max-heap
nums = [20, 1, 5, 15, 3, 10]

# Use _heapify_max to transform the list into a max-heap
heapq._heapify_max(nums)
print(f"Max-heap: {nums}")

# After _heapify_max, the largest element is at the root
# To pop the largest element, swap the first and last element, reduce the size, and heapify
nums[0], nums[-1] = nums[-1], nums[0]
max_element = nums.pop()  # Remove the last element, which is now the largest
heapq._heapify_max(nums)  # Restore the max-heap property
print(f"Max element: {max_element}")
print(f"Heap after popping max element: {nums}")





heapq.heappush(B, -7) # Insert 7 into max heap

print(B)


# Build heap from scratch - Time: O(n log n)

C = [-5, 4, 2, 1, 7, 0, 3]

heap = []

for x in C:
  heapq.heappush(heap, x)
  print(heap, len(heap)) # Check size of heap

# !Putting tuples of items on the heap

D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

from collections import Counter

counter = Counter(D)

print(counter)

heap = []

for k, v in counter.items():
  heapq.heappush(heap, (v, k))

print(heap)