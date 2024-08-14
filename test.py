# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Sll:
#     def __init__(self):
#         self.head = None

#     def transversal(self):
#         a = self.head

#         if a is None:
#             print("Single list is empty")
        
#         else:
#             while a is not None:
#                 print(a.data, end="  ")
#                 a = a.next
            
#     def insert_at_beginning(self, data):
#         print()
#         nb = Node(data)
#         nb.next = self.head
#         self.head = nb

#     def insert_at_end(self,data):
#         print()
#         ne = Node(data)
#         a = self.head
#         while a.next is not None:
#             a = a.next
#         a.next = ne
    
#     def insert_at_specififed_node(self, position, data):
#         print()
#         nib = Node(data)
#         a = self.head
#         for i in range(1, position-1):
#             a = a.next
#         nib.next = a.next
#         a.next = nib

#     def deletion_at_beginning(self):
#         print()
#         a = self.head
#         self.head = a.next
#         a.next = None

#     def deletion_at_end(self):
#         print()
#         prev = self.head
#         a = self.head.next

#         while a.next is not None:
#             a = a.next
#             prev = prev.next

#         prev.next = None

#     def delete_at_specified_node(self, position):
#         print()
#         prev = self.head
#         a = self.head.next

#         for i in range(1, position-1):
#             a = a.next
#             prev = prev.next
#         prev.next = a.next
#         a.next = None
        

# n1 = Node(5)
# sll = Sll()
# sll.head= n1
# n2 = Node(10)
# n1.next = n2
# n3 = Node(15)
# n2.next = n3
# n4 = Node(20) 
# n3.next = n4

# sll.transversal()
# sll.insert_at_beginning(0)
# sll.transversal()
# sll.insert_at_end(25)
# sll.transversal()
# sll.insert_at_specififed_node(6,22)
# sll.transversal()
# sll.deletion_at_beginning()
# sll.transversal()
# sll.deletion_at_end()
# sll.transversal()
# sll.delete_at_specified_node(3)
# sll.transversal()

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None



# 

# def two_sum(nums, target):
#     # Dictionary to store the value and its index
#     num_to_index = {}
    
#     # Iterate through the list
#     for index, num in enumerate(nums):
#         # Calculate the complement of the current number
#         complement = target - num
        
#         # Check if the complement is already in the dictionary
#         if complement in num_to_index:
#             # If found, return the indices of the complement and the current number
#             return [num_to_index[complement], index]
        
#         # If not found, store the number and its index in the dictionary
#         num_to_index[num] = index
    
#     # If no solution is found, return an empty list or handle as needed
#     return []

# # Example usage
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))  # Output: [0, 1]


# def two_sum(nums, target):
#     nums_to_index = {}

#     for index, num in enumerate(nums):
#         complement = target - num

#         if complement  in nums_to_index:
#             return [nums_to_index[complement], index]
        
#         else:
#             nums_to_index[num] = index

#     return[]


# nums = [2, 5, 6, 7, 8, 0]
# target = 20
# sens= two_sum(nums, target)
# print(sens)



# def solution(num, target):
#     nums_to_index = {}

#     for index, nums in enumerate(num):
#         complement = target - nums

#         if complement in nums_to_index:
#             return nums_to_index[complement] , index
#         else:
#             nums_to_index[nums] = index
                
#     return[]
    
# num = [2,3,4,5,5,6]
# target = 9

# clear = solution(num, target)
# print(clear)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None


# class Dll:
#     def __init__(self):
#         self.head = None

#     def forward_transversal(self):
#         if self.head is None:
#             print("Double Linked List is empty")
        
#         a = self.head
#         while a is not None:
#             print(a.data, end="---->")
#             a = a.next


#     def backward_transversal(self):
#         if self.head is None:
#             print("Double Linked List is empty")

#         a = self.head

#         while a.next is not None:
#             a = a.next
#         while a is not None:
#             print(a.data, end="<----")
#             a = a.prev

#     def insertion_at_beginning(self, data):
#         print()
#         ne = Node(data)
#         a = self.head
#         a.prev = ne
#         ne.next = a
#         self.head = ne

#     def insertion_at_end(self, data):
#         print()
#         np = Node(data)
#         a = self.head
#         while a.next is not None:
#             a = a.next
#         a.next = np
#         np.prev = a 

#     def insertion_at_specific_node(self, position, data):
#         print()
#         nib = Node(data)
#         prev = self.head
#         a = self.head.next

#         for i in range(1, position-1):
#             a = a.next
#             prev = prev.next
#         prev.next = nib
#         nib.prev = prev
#         nib.next = a
#         a.prev = nib

#     def deletion_at_beginning(self):
#         print()
#         prev = self.head
#         a = self.head.next
#         self.head = a
#         a.prev = None
#         prev.next = None

#     def deletion_at_end(self):
#         print()
#         prev = self.head
#         a = self.head

#         while a.next is not None:
#             a = a.next 
#             prev = prev.next
        
#         prev.next = None
#         a.prev = None

#     def deletion_at_specific_node(self, position):
#         prev = self.head
#         a = self.head.next

#         for i in range(1, position-1):
#             a = a.next
#             prev = prev.next
#         prev.next = a.next
#         a.next.prev = prev
#         a.prev = None
#         a.next = None



# n1 = Node('Banana')
# dll = Dll()
# dll.head = n1
# n2 = Node('Mango')
# n2.prev = n1
# n1.next = n2
# n3 = Node('Orange')
# n3.prev = n2
# n2.next =n3
# n4 = Node('Grape')
# n4.prev = n3
# n3.next = n4
# dll.forward_transversal()
# dll.backward_transversal()
# dll.insertion_at_beginning('Guava')
# dll.forward_transversal()
# dll.backward_transversal()
# dll.insertion_at_end('Casava')
# dll.forward_transversal()
# dll.backward_transversal()
# dll.insertion_at_specific_node(4, 'Melon')
# dll.forward_transversal()
# dll.backward_transversal()
# dll.deletion_at_beginning()
# dll.forward_transversal()
# dll.backward_transversal()
# dll.deletion_at_end()
# dll.forward_transversal()
# dll.backward_transversal()
# dll.deletion_at_specific_node(3)
# dll.forward_transversal()
# dll.backward_transversal()


# class TreeNode:
#     def __init__(self, data ):
#         self.data = data
#         self.children = []
#         self.parent = None

#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)

#     def get_level(self):
#         level = 0
#         p = self.parent

#         while p:
#             level+=1
#             p = p.parent
#         return level
    
#     def print_tree(self):
#         space = " " * self.get_level() * 3
#         prefix = space + "|__" if self.parent else ""
#         print(prefix + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_tree()

# def build_tree():
#     root = TreeNode("Electronics")

#     laptop = TreeNode("Laptops")

#     laptop.add_child(TreeNode("Mac"))

#     laptop.add_child(TreeNode("Windows"))

#     laptop.add_child(TreeNode("HP"))

#     tv = TreeNode("TV")

#     tv.add_child(TreeNode("LG"))

#     tv.add_child(TreeNode("Hisense"))

#     tv.add_child(TreeNode("Panasonic"))

#     smartphone = TreeNode("Smartphone")

#     smartphone.add_child(TreeNode("Iphone"))

#     smartphone.add_child(TreeNode("Samsung"))

#     smartphone.add_child(TreeNode("Nokia"))


#     root.add_child(laptop)
#     root.add_child(smartphone)
#     root.add_child(tv)

#     root.print_tree()


# if __name__ == '__main__':
#     build_tree()


# B = [False, False, False, False, True, True]

# def binary_search_condition(arr):
#     N = len(arr)
#     L = 0
#     R = N - 1

#     while L < R:
#         M = (L + R) // 2

#         if B[M]:
#             R = M

#         else:
#             L = M + 1

#     return L


# root =binary_search_condition(B)
# print(root)


# n = 10
# A = [[2, 5], [2, 0], [5, 1], [5, 10], [0, 8], [0, -4], [1, 3], [1, 12], [10, 9]]

# from collections import defaultdict

# D = defaultdict(list)

# for u,v in A:
#     D[u].append(v)

# print(D)


# def dfs_recursive(node):
#     print(node)
#     for nei_node in D[node]:
#         if nei_node not in seen:
#             seen.add(nei_node)
#             dfs_recursive(nei_node)


# source = 2
# seen = set()   
# seen.add(source) 
# dfs_recursive(source)   



# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.neighbour = []

#     def __str__(self):
#         return f"Node {self.value}"

#     def display(self):
#         connections = [node.value for node in self.neighbour]
#         return f"{self.value} is connected to {connections}"


# A = Node('Jesus is Lord')
# B = Node("Jesus is God revealed to man")
# C = Node("Jesus died and rose on the third")
# D = Node("Jesus ascended to heaven")

# A.neighbour.append(B)
# B.neighbour.append(A)

# C.neighbour.append(D)
# D.neighbour.append(C)

# print(A.display())



# D = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

# def merge_sort(arr):
#     n = len(arr)

#     if n ==1:
#         return arr
    
#     m = len(arr) // 2

#     L = arr[:m]
#     R = arr[m:]

#     L = merge_sort(L)
#     R = merge_sort(R)

#     L_len = len(L)
#     R_len = len(R)

#     l,r = 0,0
#     new_list = [0] * n
#     i = 0

#     while l < L_len and r < R_len:
#         if L[l] < R[r]:
#             new_list[i] = L[l]
#             l += 1
#         else:
#             new_list[i] = R[r]
#             r += 1
        
#         i += 1
    
#     while l < L_len:
#         new_list[i] = L[l]
#         l += 1
#         i += 1

#     while r < R_len:
#         new_list[i] = R[r]
#         r += 1
#         i += 1

#     return new_list

# heapo = merge_sort(D)
# print(heapo)


    


# E = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

# def quick_sort(arr):
#     n = len(arr)
#     if n <= 1:
#         return arr
    
#     pivot = arr[-1]


#     L = [x for x in arr[:-1] if x <= pivot]
#     R = [x for x in arr[:-1] if x > pivot]

#     L = quick_sort(L)
#     R = quick_sort(R)


#     return L + [pivot] + R

# quick = quick_sort(E)


# print(quick)





# E = [-5, 3, 2, 1, -3, -3, 7, 2, 2]


# def counting_sort(arr):
#     n = len(arr)
#     maxx = max(arr)
#     counts = [0] * (maxx + 1)

#     for x in arr:
#         counts[x] += 1

#     i = 0
#     for c in range(maxx + 1):
#         while counts[c] > 0:
#             arr[i] = c
#             i += 1
#             counts[c] -= 1

    
# deep= counting_sort(E)
# print(deep)





# def bottom_down(n):
#     if n == 0:
#         return 0
    
#     if n == 1:
#         return 1
    
#     prev = 0
#     cur = 1

#     for i in range(2 , n+ 1):
#         prev , cur = cur , prev + cur

#     return cur

# Jesusislord = bottom_down(7)
# print(Jesusislord) 



# def bottom_up(n):
#     if n == 0:
#         return 0
    
#     if n == 1:
#         return 1
    
#     dp = [0] * (n + 1)
#     dp[0] = 0
#     dp[1] = 1

#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]

#     return dp[n]

# Godisreal = bottom_up(10)
# print(Godisreal)


# def top_down(n):
#     memo = {0 : 0, 1 : 1}

#     if n in memo:
#         return memo[n]
    
#     else:
#         memo[n] = top_down(n - 1) + top_down(n - 2)
#         return memo [n]
    

# podcast = top_down(7)
# print(podcast)