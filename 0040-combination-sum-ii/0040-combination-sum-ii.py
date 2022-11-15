class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
        candidates.sort()
        
        def _cs2(target, ptr):
            if target == 0:
                res.append(curr[:])
                return
            
            if target < 0 or ptr == len(candidates):
                return
            
            curr.append(candidates[ptr])
            _cs2(target - candidates[ptr], ptr + 1)

            curr.pop()
            while ptr + 1 < len(candidates) and candidates[ptr] == candidates[ptr + 1]:
                ptr += 1
            _cs2(target, ptr + 1)
            
        _cs2(target, 0)
        return res
            
        