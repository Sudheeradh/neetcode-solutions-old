class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rank = [1] * (n + 1)
        parent = [i for i in range(n + 1)]
        
        def find(parent, node):
            while parent[node] != node:
                node = parent[node]
            return node
        
        def union(edge):
            a, b = find(parent, edge[0]), find(parent, edge[1])
            if rank[a] < rank[b]:
                a, b = b, a
            
            rank[a] += 1
            parent[b] = a
        
        for edge in edges:
            a, b = edge
            if find(parent, a) == find(parent, b):
                return edge
            
            union(edge)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(edges)
#         par = [i for i in range(n + 1)]
#         rank = [1 for _ in range(n + 1)]
        
#         def find(node, par):
#             if node == par[node]:
#                 return par[node]
#             else:
#                 return find(par[node], par)
        
#         def union(node_a, node_b, par, rank):
#             par_a = find(node_a, par)
#             par_b = find(node_b, par)
#             if rank[par_a] < rank[par_b]:
#                 par_a, par_b = par_b, par_a
#             par[par_b] = par_a
#             rank[par_a] += 1
        
#         for a, b in edges:
#             if find(a, par) == find(b, par):
#                 return [a, b]
#             else:
#                 # print(a, b)
#                 union(a, b, par, rank)