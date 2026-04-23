#This program is used to understand Topological sort using DFS algorithm.
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

def DFS(node,graph,visited,result):
    if not visited[node]:
        visited[node]=True
        for ngbr in graph[node]:
            DFS(ngbr,graph,visited,result)
        result.append(node)


def topological_sort(graph):
    visited=defaultdict(bool)
    result=deque()
    for i in graph.keys():
        if not visited[i]:
            DFS(i,graph,visited,result)
    while result:
        a=result.pop()
        print(a,end=",")

topological_sort(graph)