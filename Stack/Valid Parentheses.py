class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        bracketMap = {"}":"{", "]":"[", ")":"("}
        for i in s:
            if i in bracketMap.values():
                ls.append(i)
            elif(len(ls) == 0):
                return False
            else:
                if bracketMap[i] != ls.pop():
                    return False
        if len(ls) != 0:
            return False
        return True