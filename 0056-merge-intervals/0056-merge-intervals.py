class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        intervals.append([float('inf'), float('inf')])
        res = []
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if curr[1] < intervals[i][0]:
                res.append(curr)
                curr = intervals[i]
            
            curr[1] = max(curr[1], intervals[i][1])
        return res 