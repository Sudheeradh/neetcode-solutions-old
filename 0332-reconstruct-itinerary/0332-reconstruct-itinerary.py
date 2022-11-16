from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        hmap = defaultdict(list)
        n = len(tickets)
        
        for ticket in tickets:
            hmap[ticket[0]].append([ticket[1], False])
            
        for airport in hmap:
            hmap[airport].sort(key = lambda x: x[0])
        
        res = []
        cnt = [0]
        
        def dfs(airport):
            if cnt[0] == n:
                return True
            
            if airport not in hmap:
                return False
            
            for neighbour in hmap[airport]:
                if neighbour[1]:
                    continue
                
                cnt[0] += 1
                neighbour[1] = True
                if dfs(neighbour[0]) == True:
                    res.append(neighbour[0])
                    return True
                
                neighbour[1] = False
                cnt[0] -= 1
                
        
        dfs("JFK")
        res.append("JFK")
        res.reverse()
        return res