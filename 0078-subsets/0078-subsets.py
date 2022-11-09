class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        
        def backtrack(subset, i):
            if i == len(nums):
                res.append(subset)
                return
            
            backtrack(subset[:], i + 1)
            
            subset.append(nums[i])
            backtrack(subset[:], i + 1)
        
        backtrack(subset, 0)
        return res
        
        