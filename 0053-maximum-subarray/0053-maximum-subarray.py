class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r, curr_sum, max_sum = 0, 0,  float('-inf')
        
        while r != len(nums):
            curr_sum += nums[r]
            max_sum = max(curr_sum, max_sum)
            if curr_sum < 0:
                curr_sum = 0
            r += 1
        
        return max_sum
        