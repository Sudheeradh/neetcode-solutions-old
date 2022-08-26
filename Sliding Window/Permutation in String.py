class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return s1 == s2
        
        hashMap_s1 = {}
        for i in s1:
            hashMap_s1[i] = 1 + hashMap_s1.get(i, 0)
        l = 0
        r = len(s1) - 1
        
        hashMap_window = {}
        for i in range(r):
            hashMap_window[s2[i]] = 1 + hashMap_window.get(s2[i], 0)
            
            
        while r < len(s2):
            hashMap_window[s2[r]] = 1 + hashMap_window.get(s2[r], 0)
            
            if hashMap_s1 == hashMap_window:
                return True
            
            if hashMap_window[s2[l]] == 1:
                hashMap_window.pop(s2[l])
            else:
                hashMap_window[s2[l]] -= 1
            r += 1
            l += 1
        return False