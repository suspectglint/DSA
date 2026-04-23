#Kahn's Algorithm/Topological Sort using BFS
#This program is used to understand Topological sort using BFS algorithm.
"""
What is Topological Sort?
Given a Directed Acyclic Graph, Topological sort prints out elements in expected order as present in graph i.e. if we have two nodes a and b where a appears b(a->b)
when we topologically sort it the output will ensure a appears b and similarly for other edges(nodes).

A topological sort of a Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u→v, vertex u appears before vertex v in the ordering. 
This ensures that all dependencies represented by edges are respected.
"""
from collections import deque,defaultdict

graph={
    1:[2],
    2:[3,7,8],
    3:[9],
    6:[],
    7:[6,8],
    8:[9],
    9:[]
}

def topo_BFS(graph):
    indegree=defaultdict(int)
    queue=deque()
    result=[]
    for node in graph.keys():
        indegree[node]=0
    for lst in graph.values():
        for i in lst:
            indegree[i]+=1
    for i in indegree:
        if indegree[i]==0:
            queue.append(i)
    while queue:
        a=queue.popleft()
        result.append(a)
        for i in graph[a]:
            indegree[i]-=1
            if indegree[i]==0:
                queue.append(i)
    print(result)


topo_BFS(graph)