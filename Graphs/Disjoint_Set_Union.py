"""
Union-Find algorithm 

This algorithm is used to build disjoint sets in a given graph by using union and find.
Explanation for this is present in Kruskal's algorithm.
"""
class DSU:
    
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
        self.Parent=list(range(n+1))
        """
        The size is used for union by size. for example, when we are combining two components, this size
        will be used to decide which of the two parents will be made as parent of the combined component.
        Ideally the one with the larger size will be made parent as that will decrease the height of the overall component.
        """
        self.Size=[1]*(n+1)
    
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
        if self.Parent[node]!=node:
            self.Parent[node]=self.find(self.Parent[node])
        return self.Parent[node]

    """
    This method is used to combine two nodes(more like components of that node) into one node by checking the proper eligibility.
    First, we check whether the two nodes belong to same component, if they are then we cannot combine these two as it will form a loop.
    And if they donot belong to same component, we union these two components based on union by size.
    union byy size - when we are combining two components, we need to decide among the two ultimate parents and choose one ultimate parent
    for the combined component.
    """
    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)
        if pu == pv:
            return False
        self.comps-=1
        if self.Size[pu] < self.Size[pv]:
            pu,pv = pv,pu
        self.Size[pu]+=self.Size[pv]
        self.Parent[pv]=pu
        return True
    
    def components(self):
        return self.comps
    
class Solution:
    def validTree(self, n, edges) :
        if len(edges) > n - 1:
            return False

        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        return dsu.components() == 1

sol=Solution()
a=sol.validTree(5,[[0,1],[1,2],[1,3],[1,4]])
print(a)