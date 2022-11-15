class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        a = ord("a")
        p = ord("p")
        
        i = 0
        hmap = {}
        while i != p - a:
            if ((i // 3) + 2) not in hmap:
                hmap[(i // 3) + 2] = [chr(i + a)]
            else:
                hmap[(i // 3) + 2].append(chr(i + a))
            i += 1
        hmap[7] = ["p", "q", "r", "s"]
        hmap[8] = ["t", "u", "v"]
        hmap[9] = ["w","x","y","z"]
        
        res = [""]
        for i in digits:
            temp = []
            for j in res:
                for k in hmap[int(i)]:
                    temp.append(j + k)
            res = temp[:]
            
        
        return res