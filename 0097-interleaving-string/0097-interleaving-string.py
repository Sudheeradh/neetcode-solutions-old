class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        
        def _ii(s1, s2, s3, i, j, k, memo):
            key = (i, j, k)
            
            if key in memo:
                return memo[key]
            
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            
            if i > len(s1) or j > len(s2) or k > len(s3):
                return False
            
            left, right = False, False
            if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
                left = _ii(s1, s2, s3, i + 1, j, k + 1, memo)
            
            if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
                right = _ii(s1, s2, s3, i, j + 1, k + 1, memo)
                
            memo[key] = left or right
            return memo[key]
        
        return _ii(s1, s2, s3, 0, 0, 0, {})
            