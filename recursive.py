# Fibonacci
# F(0) = 0
# F(1) = 1
# n > 1: F(n) = F(n-1) + F(n-2)
# ! Time Complexity: O(2^n)
# * Space Complexity O(n)

def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n - 2)
    
# print(F(0))

class SingleNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
Head = SingleNode(1)
A = SingleNode(3)
B = SingleNode(4)
C = SingleNode(7)

Head.next = A
A.next = B
B.next = C



# print(Head)
#? Time complexity : O(n)
#! Space complexity : O(n)

def reverse(node):
    if not node:
        return None
    
    reverse(node.next)
    print(node)

# reverse(Head)
