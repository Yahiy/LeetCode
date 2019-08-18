#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
https://algs4.cs.princeton.edu/44sp/
https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
http://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
"""
import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt


class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.nodes = []
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
        if from_node not in self.nodes:
            self.nodes.append(from_node)
        if to_node not in self.nodes:
            self.nodes.append(to_node)

def creat_graph():
    edges = [
        ('A', 'B', 7),
        ('A', 'C', 2),
        ('A', 'F', 2),
        ('B', 'D', 3),
        ('B', 'F', 3),
        ('C', 'E', 4),
        ('C', 'L', 2),
        ('D', 'F', 1),
        ('F', 'H', 3),
        ('G', 'H', 2),
        ('G', 'Y', 2),
        ('I', 'K', 4),
        ('I', 'L', 4),
        ('I', 'X', 3),
        ('J', 'L', 1),
        ('J', 'H', 1),
        ('J', 'X', 9),
        ('K', 'Y', 5),
    ]
    graph = Graph()
    for edge in edges:
        graph.add_edge(*edge)
    print(graph.edges)
    print(sorted(graph.nodes))
    return graph, edges

def show_graph(edges):
    # G = nx.MultiDiGraph()
    G = nx.MultiGraph()
    for (n1,n2,e) in edges:
        G.add_edge(n1,n2, weight=int(e))
    edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
    spring_pos = nx.spring_layout(G)
    plt.axis("off")
    nx.draw_networkx_edge_labels(G,spring_pos,edge_labels=edge_labels)
    nx.draw_networkx(G, pos = spring_pos, with_labels = True, node_size = 250, node_color='g')
    plt.show()

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend([x for x in graph[vertex] if x not in visited])
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend([x for x in graph[vertex] if x not in visited])
    return visited

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

graph, edges = creat_graph()
show_graph(edges)
print(dfs(graph.edges, 'A'))
print(bfs(graph.edges, 'A'))
print(list(dfs_paths(graph.edges, 'A', 'C')))
print(list(bfs_paths(graph.edges, 'A', 'C')))



