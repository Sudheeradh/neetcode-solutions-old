class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map = {}
        for i in range(len(s)):
            map[s[i]] = i
        
        count = 0
        res = []
        curr_end = 0
        for i in range(len(s)):
            if curr_end < map[s[i]]:
                curr_end = map[s[i]]
            count += 1
            if i == curr_end:
                res.append(count)
                count = 0
        return res

