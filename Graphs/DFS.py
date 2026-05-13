#This program is used to implement Depth First Search(DFS) for trees and graphs.

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

#Root->left->right(Rlr)
def DFS_tree_preorder(root):
    if not root:
        return
    print(root.val,end='-->')
    DFS_tree_preorder(root.left)
    DFS_tree_preorder(root.right)
    
#left->Root->right(lRr)
def DFS_tree_inorder(root):
    if not root:
        return
    DFS_tree_inorder(root.left)
    print(root.val,end='-->')
    DFS_tree_inorder(root.right)

#left->right->Root(lrR)
def DFS_tree_postorder(root):
    if not root:
        return
    DFS_tree_postorder(root.left)
    DFS_tree_postorder(root.right)
    print(root.val,end='-->')

#Recursive solution for DFS in Graphs.
"""
Algorithm :
Recursive is straight-forward.
We pass the adj_list, node and visited_set as arguments to the function.
At start of the function, we check whether node is visited or not.
If visited, we just return.
If not visited, we add it to visited_set and add it to traversal path.
Now to pick the next node for traversal.
We iterate through nodes in adjacency list.
But for each node, we call the function recursively. 
This ensures we are traversing the graph depth wise.
"""
def DFS_graph_recursive(adj_list,node,visited):
    #print(adj_list,visited,node)
    if node in visited:
        return
    print(node,end="-->")
    visited.add(node)
    for n in adj_list[node]:
        DFS_graph_recursive(adj_list,n,visited)

#Iterative solution for DFS in Graphs:
"""
Algorithm :
->In the iterative approach, we use a stack to traverse depth wise.
->We start off by inserting a starting node into stack.
->Start iteration and iterate until stack is non-empty.
->At every step we pop the node from stack that is last inserted.
->And we check if the node is visited or not and proceed ahead.
->If not visited, we mark it visited and add it to traversal path.
->Then we need to add all the nodes adjacent to this popped node from adjacenct list.
->However we reverse this adjacency list and add nodes to the stack, so that the first node in adjacency
  list is inserted last and it will be the first node out.(LIFO)
->This way we are making sure the traversal is depth wise.
"""
def DFS_graph_iterative(adj_list,node):
    visited_set = set()
    stack = [node]
    while stack:
        cnode=stack.pop()

        if cnode in visited_set:
            continue
        visited_set.add(cnode)
        print(cnode,end="-->")
        for i in reversed(adj_list[cnode]):
            stack.append(i)

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

visited_set=set()

DFS_graph_recursive(graph,0,visited_set)
print()
DFS_graph_iterative(graph,0)