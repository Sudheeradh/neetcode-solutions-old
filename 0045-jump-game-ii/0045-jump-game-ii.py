class Solution:
    def jump(self, nums: List[int]) -> int:
#         goal = len(nums) - 1
#         ptr = goal
#         min_pos_ptr = goal
#         steps = 0
        
#         while goal > 0:
#             while ptr > 0:
#                 ptr -= 1
#                 if goal - ptr <= nums[ptr]:
#                     min_pos_ptr = min(ptr, min_pos_ptr)
#             steps += 1
#             goal = min_pos_ptr
#             ptr = goal
        
#         return steps

        l, r = 0, 0
        res = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
        
        