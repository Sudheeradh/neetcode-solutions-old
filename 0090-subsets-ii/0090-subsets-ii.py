from bisect import bisect_left
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = [[]]
        nums.sort()
        
        def _swd(ptr):
            if ptr >= len(nums):
                return
            
            curr.append(nums[ptr])
            res.append(curr[:])
            _swd(ptr + 1)
            
            curr.pop()
            _swd(bisect_left(nums,nums[ptr] + 1))
        
        _swd(0)
        
#         for i in range(len(res)):
#             res[i] = tuple(sorted(res[i]))
        
#         res = list(set(res))
        return res
        
        
            