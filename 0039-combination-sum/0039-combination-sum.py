class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        
        def _cs(target, ptr):
            if target < 0 or ptr == len(candidates):
                return
            
            if target == 0:
                res.append(curr[:])
            
            curr.append(candidates[ptr])
            _cs(target - candidates[ptr], ptr)
            curr.pop()
            _cs(target, ptr + 1)
        
        _cs(target, 0)
        for i in range(len(res)):
            res[i] = tuple((res[i]))
        res = list(set(res))
        return res
        