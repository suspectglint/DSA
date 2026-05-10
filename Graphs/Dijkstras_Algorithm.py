"""
Dijkstra's algorithm is a greedy algorithm used to find the shortest path from a source node 
to all other nodes in a weighted graph.
It works only for graphs with non-negative edge weights and undirected graph.
Dijkstra's algorithm finds the shortest path from a given source node to every other node.
It can be used to find the shortest path to a specific destination node, by terminating the 
algorithm after determining the shortest path to that node.
"""

"""
Algorithm :-
-> The idea is to traverse from source node to all the nodes and update the minimum distance along the 
   way for each node if applicable.(If the current distance calculated for a given node is less than
   the already present distance.)
-> We need following key data structures :-
    1. min_dist - to store the minimum distance from source node to every other node in the graph.
    2. pre_node - to store the previous node of the shortest path for a given node.
      (Useful for traversing the shortest path)
    3. min_dist_heap - used to pickup the current shortest path using heap implementation.
    This is initialized with (0,source)[(distance,node)] as the distance from source to source is zero.
    4. visited_set - to store all the visited nodes.(nodes for which minimum distance is calculated.)
-> At every iteration, we pick the node from min_dist_heap with the shortest distance and proceed only
   if it is not visited yet. And we pick all the neighbours of that node and calcualte the distance by adding
   the current node's distance from source and the edge between current node and neigbbour. If the distance is 
   less than the already stored minimum distance, we update the minimum distance of that neighbour node in min_dist 
   and add the node to min_dist_heap. And update the prev_node as well to store the previous node as current node.
-> This iteration continues until thee min_dist_heap is non-empty.
-> At the end of algorithm, we have min_dist and prev_node with correct values.
"""

import math
import heapq

#Input graph for this algorithm and here we are considering source as "0"
graph = {
    0 : [(1,4),(2,8)],
    1 : [(0,4),(4,6),(2,3)],
    2 : [(0,8),(1,3),(3,2)],
    3 : [(2,2),(4,10)],
    4 : [(1,6),(3,10)]
}
print(graph)


# dist - for storing the minimum distance from source to a given node.
min_dist = {
    0 : 0,
    1 : math.inf,
    2 : math.inf,
    3 : math.inf,
    4 : math.inf
}

#node - store previous node for each node of the minimum distance path.
#(this is for retracing the minimum distance path from any node to source.)
prev_node = {
    0 : None,
    1 : None,
    2 : None,
    3 : None,
    4 : None
}

min_dist_heap = [(0,0)]
heapq.heapify(min_dist_heap)

visited_set = set()

while min_dist_heap:
    dist,node = heapq.heappop(min_dist_heap)
    if node in visited_set:
        continue
    for nnode,ndist in graph[node]:
        if nnode not in visited_set:
            if dist+ndist < min_dist[nnode]:
                min_dist[nnode]=dist+ndist
                prev_node[nnode]=node
                heapq.heappush(min_dist_heap,(min_dist[nnode],nnode))
    visited_set.add(node)

print(visited_set)
print(min_dist)
print(prev_node)