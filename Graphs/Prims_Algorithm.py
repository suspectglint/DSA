"""
Prim's Algorithm - this algorithm is used for finding minimum spanning tree(MST) in a given graph.
Minimum Spanning Tree - for a given graph G(V,E), a tree connecting all the vertices V using V-1 edges,no cycles
and has the minimum possible total edge weight is called a minimum spanning tree.
"""

"""
Intuition :-
The basic idea of Prim's algorithm is to start off from any vertex and pick the edge with the least
weight(from a visited node to an unvisited node). Repeat the process until all nodes are visited. 

Data Structues used :-
1. Visited_set :- to mark whether a given vertex is visited or not.(adding vertex to this set marks it as visited.)
2. min_heap - this heap is used to pick the edge with least weight.
3. mst - to store the edges of the minimum spanning tree.
4. mst_cost - to store total cost of minimum spanning tree.

Algorithm :-

Initialization:
We initialize min_heap with [0,src,-1]([weight,src,parent]) - for source vertex, we are marking weight as 0
and parent as -1.

Iteration: 

-> We iterate until the min_heap is non-empty.
-> Pop the minimum weight edge from min_heap.
-> Check whether src is already visited, if yes skip iteration and continue to next edge.
-> If src is not visted, mark it visited and proceed to processing edges.
-> Before processing, add the edge to mst by ignoring the src node first as that is a pseudo edge.
-> For src, pick each edge and check if the vertex is visited.
-> If edge vertex is not visited, add heappush it to the min_heap.
"""
import heapq

#Input graph for this algorithm and let's choose starting vertex as 3
graph = {
    0 : [(1,4),(2,8)],
    1 : [(0,4),(4,6),(2,3)],
    2 : [(0,8),(1,3),(3,2)],
    3 : [(2,2),(4,10)],
    4 : [(1,6),(3,10)]
}
print(graph)

min_heap = []

#Picking a source vertex and adding minimum edge from source to min_heap
src=3
min_heap.append([0,src,-1])
visited_set = set()
mst = []
mst_cost = 0

while min_heap:
    weight,vertex,parent = heapq.heappop(min_heap)
    if vertex in visited_set:
        continue
    if parent!=-1:
        mst.append([parent,vertex,weight])
        mst_cost+=weight
    visited_set.add(vertex)
    for ver,wgt in graph[vertex]:
        if ver in visited_set:
            continue
        heapq.heappush(min_heap,[wgt,ver,vertex])

print(mst)
print(mst_cost)