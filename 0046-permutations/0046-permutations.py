class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if nums == []:
            return [[]]
        
        first = nums[0]
        remaining = nums[1:]
        perms = self.permute(remaining)
        res = []
        
        for perm in perms:
            for i in range(len(perm) + 1):
                res.append(perm[:i] + [first] + perm[i:])
        
        return res
    