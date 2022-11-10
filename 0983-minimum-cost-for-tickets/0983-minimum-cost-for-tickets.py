from bisect import bisect_left
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        def _minCost(day, memo):
            if day in memo:
                return memo[day]
            
            i = bisect_left(days, day)
            if i == len(days):
                return 0
            
            single = costs[0] + _minCost(days[i] + 1, memo)
            week = costs[1] + _minCost(days[i] + 7, memo)
            month = costs[2] + _minCost(days[i] + 30, memo)
            
            
            memo[day] = min(single, week, month)
            return memo[day]
        
        return _minCost(days[0], {})