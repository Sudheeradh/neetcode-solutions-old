class Solution:
    def condition(self, s, t):
        for key in t.keys():
            if s.get(key, 0) < t[key]:
                return False
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        target = {}
        currWindow = {}
        for i in t:
            target[i] = 1 + target.get(i, 0)
        l, r = 0, 0
        fin_min = len(s)
        res = ""
        while r < len(s):
            currWindow[s[r]] = 1 + currWindow.get(s[r], 0)
            while (self.condition(currWindow, target)):
                if fin_min >= (r - l + 1):
                    res = s[l:r+1]
                    fin_min = r - l + 1
                currWindow[s[l]] -= 1
                l += 1
            r += 1
        return res