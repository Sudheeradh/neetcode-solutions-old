class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        def check(nums):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True
        
        nums.append(float('inf'))
        nums.insert(0, float('-inf'))
        
        if check(nums):
            return True
        
        conflict = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                conflict = i
                break
        
        main1 = nums[conflict - 1 : conflict + 3]
        main2 = nums[conflict - 1 : conflict + 3]
        main1[1] = main1[0]
        main2[2] = main2[3]
        
        if check(main1):
            nums[conflict - 1 : conflict + 3] = main1
        
        elif check(main2):
            nums[conflict - 1 : conflict + 3] = main2
        
        return check(nums)
        