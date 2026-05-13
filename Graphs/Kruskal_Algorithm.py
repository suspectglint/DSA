
import heapq

"""
graph = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4), (4, 5)],
    3: [(1, 2), (2, 4), (4, 1)],
    4: [(2, 5), (3, 1)]
}"""

graph = {
    0 : [(1,4),(2,8)],
    1 : [(0,4),(4,6),(2,3)],
    2 : [(0,8),(1,3),(3,2)],
    3 : [(2,2),(4,10)],
    4 : [(1,6),(3,10)]
}

mst = []
mst_cost = 0
visited_set  = set()
min_heap = []

for parent in graph.keys():
    for vertex,weight in graph[parent]:
        heapq.heappush(min_heap,[weight,parent,vertex])

while min_heap:
    weight,parent,vertex = heapq.heappop(min_heap)
    if parent in visited_set and vertex in visited_set:
        continue
    mst.append([parent,vertex,weight])
    mst_cost+=weight
    visited_set.add(parent)
    visited_set.add(vertex)

print(mst)
print(mst_cost)