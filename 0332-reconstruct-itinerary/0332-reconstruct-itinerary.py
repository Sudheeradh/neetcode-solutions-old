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
        
        def remaining(airport):
            cnt = 0
            for i in hmap[airport]:
                if i[1] == False:
                    cnt += 1
            return cnt
        
        def dfs(airport):
            if remaining(airport) == 0:
                if cnt[0] == n:
                    return True
                else:
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