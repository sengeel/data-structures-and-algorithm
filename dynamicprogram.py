# Fibonacci Sequence

def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n - 2)



print(F(0))

# TOP-DOWN DYNAMIC PROGRAMMING

memo = {0:0, 1:1}

def f(x):
    if x  in memo:
        return memo[x]
        
    else:
        memo[x] = f(x - 1) + f(x - 2)
        return memo[x]
            
    

# Time : O(n)
# Space : O(n)  # Space complexity is O(n) because we are storing the Fibonacci
heaa = f(6)
print(heaa)

print(memo)



# BOTTOM-UP DYNAMIC PROGRAMMING- TABULATION


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp [1] = 1

    for i in range (2, n+1):
        dp[i] = dp[i-2]  + dp[i - 1]

    return dp[n] 

poort = fib(7)
print(poort)

# Time: O(n)
# Space: O(n)

# BOTTOM-DOWN DYNAMIC PROGRAMMING

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    
    prev = 0
    cur = 1

    for i in range (2, n+1):
        prev, cur = cur, prev + cur

    return cur


thank = fibonacci(6)
print(thank)
# Time: O(n)
# Space: O(1)