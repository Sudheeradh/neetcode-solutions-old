class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal = len(nums) - 1
#         ptr = goal
#         while ptr > 0:
#             ptr -= 1
#             if goal - ptr <= nums[ptr]:
#                 goal = ptr
        
#         return goal == 0
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0
        