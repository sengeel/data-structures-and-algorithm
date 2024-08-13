B = [-4, -1, 0, 3, 10]


def pointers(arr):
    n = len(arr)
    left = 0
    right = n - 1

    results = []

    while left<=right:
        if abs(arr[left]) > abs(arr[right]):
            results.append(arr[left] ** 2)
            left += 1
        
        else:
            results.append(arr[right] ** 2)
            right -= 1
        
    results.reverse()

    return results


heapper = pointers(B)
print(heapper)