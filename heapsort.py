import heapq

# Heap Sort
# NOTE Time: O(n logn), Space: O(n)
# NOTE: O(1) Space is possible via swapping but this complex

def heap_sort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn

    return new_list
B = [-1, 2, 3, 1, -6, 7, 9]
heapp = heap_sort(B)
print(heapp)


