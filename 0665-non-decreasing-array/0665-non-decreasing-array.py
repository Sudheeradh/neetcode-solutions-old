class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        def check(nums):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True
        
        if check(nums):
            return True
        
        nums.append(float('inf'))
        nums.insert(0, float('-inf'))
        
        conflict = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                conflict = i
                break
        
        if nums[conflict] <= nums[conflict + 2]:
            nums[conflict + 1] = nums[conflict + 2]
        else:
            nums[conflict] = nums[conflict - 1]
        
        return check(nums)
        