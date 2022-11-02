"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        
        adj = {}
        visited = set()
        def explore(node, visited, graph):
            if node.val in visited:
                return
            
            if node.val not in graph:
                graph[node.val] = []
            
            for neighbour in node.neighbors:
                graph[node.val].append(neighbour.val)
            
            visited.add(node.val)
            
            for neighbour in node.neighbors:
                explore(neighbour, visited, graph)
        explore(node, visited, adj)
        
        map = {}
        for i in range(1, len(adj) + 1):
            map[i] = Node(i)
        
        for key in adj:
            for neighbour in adj[key]:
                map[key].neighbors.append(map[neighbour])
            
        return map[1]
            