# VARIABLE-SIZE SLIDING WINDOW


def length_of_longest_substring(s):
    l = 0
    longest = 0
    sett = set()
    n = len(s)

    # O(n)

    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1

        w = (r - l) + 1
        
        longest = max(longest,w)
        sett.add(s[r])
    
    return longest

# O(n) time complexity, O(n) space complexity

a = "aertofpotaer"
mountain = length_of_longest_substring(a)
print(mountain)




# FIXED-SIZE SLIDING WINDOW


def findmaxaverage(arr, k):
    n = len(arr)
    cur_sum = 0


    for i in range(k):
        cur_sum += arr[i]
    
    max_avg = cur_sum / k


    for i in range(k, n):
        cur_sum += arr[i]
        cur_sum -= arr[i-k]

        avg = cur_sum / k
        max_avg = max(max_avg, avg)

    return max_avg

B = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fools = findmaxaverage(B, 3)
print()
print(fools)
# Time : O(n)
# Space : O(1)



