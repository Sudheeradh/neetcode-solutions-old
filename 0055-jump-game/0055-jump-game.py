class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal = len(nums) - 1
        ptr = goal
        while ptr > 0:
            ptr -= 1
            if goal - ptr <= nums[ptr]:
                goal = ptr
        
        return goal == 0
        