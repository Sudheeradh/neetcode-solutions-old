class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = set(nums)
        largest = 0
        for num in nums:
            curr = 0
            if (num - 1) not in hashMap:
                curr += 1
                while ((num + curr) in hashMap):
                    curr += 1
            largest = max(largest, curr)
        return largest