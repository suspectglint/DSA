#This program is used to implement Breadth First Search(BFS) for trees and graphs.
from collections import deque

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def BFS_tree(root):
    if not root:
        return
    queue=deque([root])
    while queue:
        node=queue.popleft()
        print(node.val,end='-->')
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

def BFS_graph(adj_list,root):
    queue=deque([root])
    visited=set()
    while queue:
        node=queue.popleft()
        if node not in visited:
            print(node,end='-->')
            visited.add(node)
            for i in adj_list[node]:
                queue.append(i)

root=Node(0)
root.left=Node(1)
root.right=Node(2)
rl=root.left 
rr=root.right
rl.left=Node(3)
rl.right=Node(4)
rr.left=Node(5)
rr.right=Node(6)

BFS_tree(root)

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [],
    4: [],
    5: [],
    6: []
}

BFS_graph(graph,0)