import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        hmap = {}
        for i in range(n):
            x, y = points[i]
            for j in range(i + 1, n):
                x1, y1 = points[j]
                dist = abs(x - x1) + abs(y - y1)
                if i not in hmap:
                    hmap[i] = [[dist, j]]
                else:
                    hmap[i].append([dist, j])
                    
                if j not in hmap:
                    hmap[j] = [[dist, i]]
                else:
                    hmap[j].append([dist, i])
                    
        visited = set()
        res = 0
        minH = [[0, 0]]
        
        while len(visited) < n:
            cost, node = heapq.heappop(minH)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            
            for neighCost, neighNode in hmap[node]:
                if neighNode in visited:
                    continue
                heapq.heappush(minH, [neighCost, neighNode])
        
        return res
        
        