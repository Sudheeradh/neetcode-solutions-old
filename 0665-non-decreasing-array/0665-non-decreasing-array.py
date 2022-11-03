class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        temp, temp_ind = 0, 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                temp, temp_ind = nums[i], i
                nums[i] = nums[i + 1]
                break
        
        r1, r2 = True, True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                r1 = False
        
        nums[temp_ind] = temp
        
        if temp_ind + 2 < len(nums):
            nums[temp_ind + 1] = nums[temp_ind + 2]
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    r2 = False
        # else:
        #     r2 = False
        
        return r1 or r2
        