from collections import defaultdict

class Solution:
    
    def empty_list(self):
        return []
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(self.empty_list)
        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        return res.values()
        