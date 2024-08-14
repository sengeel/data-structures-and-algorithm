# Quick Sort
# Time: O(n log n) (Average case, technically Worst case is O(n^2))
# Space: O(n)

E = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]

    L = [x for x in arr[:-1] if x <= pivot]
    R = [x for x in arr[:-1] if x > pivot]

    L = quick_sort(L)
    R = quick_sort(R)

    return L + [pivot] + R

quick = quick_sort(E)
print(quick)







