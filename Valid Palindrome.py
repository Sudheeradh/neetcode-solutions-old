class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t = []
        for i in s:
            if ((ord(i) <= ord("z") and ord(i) >= ord("a") ) or
                (ord(i) <= ord("Z") and ord(i) >= ord("A") ) or
                (ord(i) <= ord("9") and ord(i) >= ord("0") )):
                t.append(i)
        while (len(t) > 1):
            if (t.pop() != t.pop(0)):
                return False
        return True