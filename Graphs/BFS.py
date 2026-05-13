#This program is used to implement Breadth First Search(BFS) for trees and graphs.
"""
BFS(Breadth First Search) : 

Breadth-First Search (BFS) is a graph traversal algorithm that explores nodes level by level, 
making it ideal for problems where the shortest path or minimal steps are required in unweighted graphs. 
It uses a queue to ensure nodes are visited in the order they are discovered.

We start off with a node/root and then traverse first the children of root/nodes adjacent to start node first.
We repeat this until all the nodes in the graph/tree are visited.

Data structures used :- queue
Python we are using deque(double ended queue) where we pop the nodes from left and push the nodes from right.

visited_set(for graphs) - to mark whether the given node is visited or not in the graph.

Algorithm(Tree) :-
-> Create deque with single root node in it.
-> Start iteration and loop until the deque is empty.
-> At every step pop the left node from deque using popleft method and add it to traversal result.
-> And add the children of the popped node onto deque.(starting with left most node first and lastly right most node)
-> This works for BFS in trees.

Algorithm(Graph) :-
-> Even here we use deque to store the nodes and start with starting node of graph.
-> But before processing this node, we check whether this node is visited or not using visited_set.
-> We proceed ahead only if the node is not visited and then mark the node as visited.
-> Now we add all the nodes in the adjacency list of this popped node onto deque.
-> Similar to trees, we iterate until the deque is non-empty.
"""
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

BFS_graph(graph,0)