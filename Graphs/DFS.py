#This program is used to implement Depth First Search(DFS) for trees and graphs.
from collections import deque

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def DFS_tree_preorder(root):
    if not root:
        return
    print(root.val,end='-->')
    DFS_tree_preorder(root.left)
    DFS_tree_preorder(root.right)
    

def DFS_tree_inorder(root):
    if not root:
        return
    DFS_tree_inorder(root.left)
    print(root.val,end='-->')
    DFS_tree_inorder(root.right)

def DFS_tree_postorder(root):
    if not root:
        return
    DFS_tree_postorder(root.left)
    DFS_tree_postorder(root.right)
    print(root.val,end='-->')

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

DFS_tree_preorder(root)
print()
DFS_tree_inorder(root)
print()
DFS_tree_postorder(root)
print()

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [],
    4: [],
    5: [],
    6: []
}
