class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        res = 0
        while n not in seen:
            seen.add(n)
            n = sum(map(lambda x: int(x) ** 2, list(str(n))))
        return n == 1
            