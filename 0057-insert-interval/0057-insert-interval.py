class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []:
            return [newInterval]
        
        res = []
        
        def overlap(interval_a, interval_b):
            return not (interval_a[1] < interval_b[0] or interval_b[1] < interval_a[0])
        
        for i in range(len(intervals)):
            if not overlap(intervals[i], newInterval):
                if newInterval[1] < intervals[i][0]:
                    res.append(newInterval)
                    return res + intervals[i:]
                res.append(intervals[i])
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
                # if i == len(intervals) - 1:
                #     res.append(newInterval)
        
        # if intervals[-1][1]  < newInterval[0]:
        res.append(newInterval)
        
        return res
                
                
        
        
        