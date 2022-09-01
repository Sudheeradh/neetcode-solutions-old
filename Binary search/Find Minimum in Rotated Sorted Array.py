class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while(l <= r):
            mid = (l + r) // 2
            if (nums[mid] < nums[mid - 1]):
                return nums[mid]
            if (nums[l] < nums[l - 1]):
                return nums[l]
            if (nums[l] <= nums[mid]):
                l = mid + 1
            else:
                r = mid - 1