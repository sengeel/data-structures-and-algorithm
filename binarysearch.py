

# Naive O(n) searching
# if 8 in A :
#     print(True)

# Traditional Binary Search - Looking up if number is in array
# Time: O(logn)
# Space: O(1)

a = [-3, -1, 0, 1, 4, 7]

def binary_search(arr, target):
    N = len(arr)
    L = 0
    R = N-1

    while L<=R:
        M = L + ((R-L)//2)

        if a[M] == target:
            return True
        
        elif target < a[M]:
            R = M - 1
        else:
            L= M + 1
    
    return False

port = binary_search(a, 0)
print(port)

# Codition Based

B = [False, False, False, True, True, True]

def binary_search_condition(arr):
    N = len(arr)
    L = 0
    R = N - 1

    while L < R:
        M = (L+R)//2

        if arr[M]:
            R = M

        else:
            L = M + 1

    return L

root = binary_search_condition(B)
print(root)
        




