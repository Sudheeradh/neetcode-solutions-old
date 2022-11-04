class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setmap = set(nums)
        max_count, count = 0, 0
        for i in nums:
            if i - 1 not in setmap:
                count = 0
                while i in setmap:
                    count += 1
                    setmap.remove(i)
                    i += 1
            max_count = max(max_count, count)
        return max_count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # hashMap = set(nums)
        # largest = 0
        # for num in nums:
        #     curr = 0
        #     if (num - 1) not in hashMap:
        #         curr += 1
        #         while ((num + curr) in hashMap):
        #             curr += 1
        #     largest = max(largest, curr)
        # return largest