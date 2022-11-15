class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        
        def _cs(target):
            if target < 0:
                return
            
            if target == 0:
                res.append(curr[:])
            
            for i in candidates:
                curr.append(i)
                _cs(target - i)
                curr.pop()
        
        _cs(target)
        for i in range(len(res)):
            res[i] = tuple(sorted(res[i]))
        res = list(set(res))
        return res
        