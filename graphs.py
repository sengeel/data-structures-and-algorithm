# Array of Edges (Directed)
n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# print(A)

#? Convert array of edges to adjancency matrix

M = []
for i in range(n):
    M.append([0] * n)

# print(M)

for u, v in A:
    M[u][v] = 1

    #* Uncomment the following lines if the graph is undirected
    # ! M[v][u] = 1

# print(M)


#? Convert Array of Edges --> Adjancency list
from collections import defaultdict

D = defaultdict(list)

for u, v in A:
    D[u].append(v)

     #* Uncomment the following lines if the graph is undirected
    # ! D[v].append(u)


# print(D[3])


#? DFS with Recursion -O(V + E) where V is number of nodes and E is the number of Edges

def dfs_recursive(node):
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)


source = 0

seen = set()

seen.add(source)
dfs_recursive(source)

#? Iterative stack with DFS - O(V+E)

source = 0

seen = set()

seen.add(source)

stack = [source]


while stack:
    node = stack.pop()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node)


#? BFS (Queue) - O(V + E)
from collections import deque

source = 0
seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
    node = q.popleft()
    print (node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            q.append(nei_node)



#? Using a a class Node for storing graphs

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def __str__(self):
        return f"Node ({self.value})"

    def display(self):
        connections = [node.value for node in self.neighbors]
        return f"{self.value} is connected to {connections}"
print()

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.neighbors.append(B)
B.neighbors.append(A)

C.neighbors.append(D)
D.neighbors.append(C)

print(B.display())
