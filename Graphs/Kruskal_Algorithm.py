
import heapq

#class for defining Disjoint Set Union
class DSU:
    
    #initialization of various attributes needed to define Disjoint Set Union data structure.
    def __init__(self,n):
        """
        For storing the number of components in graph. 
        Initially, we start with 'n', where each node is a separate component
        """
        self.comps=n
        """
        For storing the parents of each node in graph.
        Initially, we define each node as it's own parent.
        """
        self.parent = [i for i in range(n+1)]
        """
        The size is used for union by size. for example, when we are combining two components, this size
        will be used to decide which of the two parents will be made as parent of the combined component.
        Ideally the one with the larger size will be made parent as that will decrease the height of the overall component.
        """
        self.size = [1]*(n+1)

    """
    This method is used to find the parent of a given node based on the component it belongs to.
    This method also implements path compression.
    Path compression - this is used to minimise the traversal for finding the parent of a given node in a component.
    For a given component, it will only have one ultimate parent. Let's say we have 4 nodes in a component and when we try to find 
    ultimate parent, we need to traverse the path from node to ultimate parent using the parents of each node across the path.
    Now, instead of this repetitive action, every time, what we do is when we traverse from node to ultimate parent, we make sure
    the parents of all the nodes along the path are also assigned to ultimate parent.
    """
    def find(self,node):
        if self.parent[node]!=node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    """
    This method is used to combine two nodes(more like components of that node) into one node by checking the proper eligibility.
    First, we check whether the two nodes belong to same component, if they are then we cannot combine these two as it will form a loop.
    And if they donot belong to same component, we union these two components based on union by size.
    union byy size - when we are combining two components, we need to decide among the two ultimate parents and choose one ultimate parent
    for the combined component.
    """
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu==pv:
            return False
        if self.size[pu] < self.size[pv]:
            pu,pv = pv,pu
        self.parent[pv] = pu
        self.size[pu] += self.size[pv]
        self.comps-=1
        return True

"""
Kruskal's algorithm - for finding minimum spanning tree.
Uses Union-Find Algorithm.(Disjoint Set Union)

Algorithm:
->Initialize a disjoint set union for n, the number of vertices in graph.
->In Kruskal, we pick the minimum weighted edge at every point and check if it forms a cycle or not.
  Based on that, we try to add the edge to MST edges.
->So to get minimum weighted edge, we have two options sorting or min_heap.
->Currently, I am using min_heap in this algorithm.
->We traverse the adjacency list and push all the edges onto min_heap.(avoiding duplicate edges.)
->Once all the edges are inserted, we start iteration by popping each edge one by one from heap
  and continue until the heap is empty.
->For every popped edge, we call the union method and see if the two components can be combined.
->If they can be combined, we add edge to mst_edges and add the weight of the edge to mst_cost.
->Towards the end, we need to check number of components in dsu and understand if it is connected or disconnected graph.
->And then, finally print the mst_edges and mst_cost.
"""
def Kruskal(graph):
    min_heap = []
    dsu = DSU(len(graph))
    for v in graph.keys():
        for u,w in graph[v]:
            if u<v:
                heapq.heappush(min_heap,[w,v,u])
    mst_edges = []
    mst_cost = 0
    #The second condition ends the loop early once we have minimum number of edges to form MST.
    while min_heap and len(mst_edges) < len(graph)-1:
        wt,a,b = heapq.heappop(min_heap)
        if dsu.union(a,b):
            mst_edges.append([a,b,wt])
            mst_cost+=wt    
    if dsu.comps>1:
        print("Disconnected Graph/Minimum Spanning Forest")
    else:
        print("Connnected Graph/Minimum Spanning Tree")
    print(mst_edges)
    print(mst_cost)
    
    

"""
graph = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4), (4, 5)],
    3: [(1, 2), (2, 4), (4, 1)],
    4: [(2, 5), (3, 1)]
}"""

"""
graph = {
    0 : [(1,4),(2,8)],
    1 : [(0,4),(4,6),(2,3)],
    2 : [(0,8),(1,3),(3,2)],
    3 : [(2,2),(4,10)],
    4 : [(1,6),(3,10)]
}"""

"""
graph = {
    0: [(1, 7), (3, 5)],
    1: [(0, 7), (2, 8), (3, 9), (4, 7)],
    2: [(1, 8), (4, 5)],
    3: [(0, 5), (1, 9), (4, 15), (5, 6)],
    4: [(1, 7), (2, 5), (3, 15), (5, 8), (6, 9)],
    5: [(3, 6), (4, 8), (6, 11)],
    6: [(4, 9), (5, 11)]
}"""

"""
graph = {
    0: []
}
"""

#"""
graph = {
    0: [(1, 1), (2, 5)],
    1: [(0, 1), (2, 2), (3, 4)],
    2: [(0, 5), (1, 2), (3, 1)],
    3: [(1, 4), (2, 1)]
}#"""


"""
graph = {
    0: [(1, 2)],
    1: [(0, 2)],
    
    2: [(3, 1)],
    3: [(2, 1)]
}
"""

print(len(graph))
Kruskal(graph)
