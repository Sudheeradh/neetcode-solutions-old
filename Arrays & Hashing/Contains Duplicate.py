class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = set()
        for num in nums:
            if num in hashMap:
                return True
            hashMap.add(num)
        return False