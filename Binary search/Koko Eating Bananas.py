class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lk = 1
        rk = max(piles)
        
        def check(k, piles, h):
            res = 0
            for i in piles:
                res += -(i // -k)
                if res > h:
                    return False
            return True
        
        while lk <= rk:
            k = (lk + rk) // 2
            if check(k, piles, h):
                rk = k - 1
            else:
                lk = k + 1
                
        if check(k, piles, h):
            return k
        else:
            return k + 1