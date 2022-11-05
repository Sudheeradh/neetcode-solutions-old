class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def _myPow(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            elif n % 2 == 0:
                res = _myPow(x, n // 2)
                return res * res
            else:
                res = _myPow(x, n // 2)
                return res * res * x
        
        res = _myPow(x, abs(n))
        
        return res if n >= 0 else 1/res
                
            
        