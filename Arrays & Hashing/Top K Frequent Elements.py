class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            hashMap[num] = 1 + hashMap.get( num, 0)
            
        ls = []
        for i in range(len(nums)):
            ls.append([])
        
        for key in list(hashMap.keys()):
            ls[hashMap[key] - 1].append(key)
            
        res = []
        i = len(ls) - 1
            
        while k > 0:
            if ls[i] != []:
                res.append(ls[i][-1])
                ls[i].pop()
                k -= 1
            else:
                i -= 1
        
        return res
                