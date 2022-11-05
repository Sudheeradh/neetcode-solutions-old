class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        res = 0
        while n not in seen:
            seen.add(n)
            n = list(str(n))
            n = map(lambda x: int(x) ** 2, n)
            n = sum(n)
        return n == 1
            