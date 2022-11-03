class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        def check(nums):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True
        
        conflict = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                conflict = i
                break
        
        conflict_val = nums[conflict]
        
        if conflict > 0:
            nums[conflict] = nums[conflict - 1]
        else:
            nums[conflict] = nums[conflict + 1]
        r1 = check(nums)
        if r1:
            return True
        
        
        nums[conflict] = conflict_val
        
        
        if conflict < len(nums) - 2:
            nums[conflict + 1] = nums[conflict + 2]
        else:
            nums[conflict + 1] = nums[conflict]
        r2 = check(nums)
        if r2:
            return True
        
        return False
        