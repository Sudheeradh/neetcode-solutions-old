class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        curr = []
        
        def _permute():
            if len(curr) == len(nums):
                if len(curr) == len(set(curr)):
                    res.append(curr[:])
                    return
                else:
                    return
            
            if len(curr) > len(nums):
                return
            
            for i in nums:
                curr.append(i)
                _permute()
                curr.pop()
        
        _permute()
        return res