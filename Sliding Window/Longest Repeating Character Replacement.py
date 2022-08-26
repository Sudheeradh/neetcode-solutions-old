class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        l, r = 0, 0
        res = 0
        for r in range(len(s)):
            hashMap[s[r]] = 1 + hashMap.get(s[r], 0)
            maxFreq = 0
            for key in hashMap.keys():
                maxFreq = max(maxFreq, hashMap[key])
            if (r - l + 1) - maxFreq <= k:
                res = max(res, r - l + 1)
            else:
                hashMap[s[l]] -= 1
                l += 1
        return res