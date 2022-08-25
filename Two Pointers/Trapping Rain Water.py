class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)
        
        lmax = 0
        for i in range(1, len(height)):
            lmax = max(lmax, height[i - 1])
            left[i] = lmax
        
        rmax = 0
        for i in range(len(height)-2, -1, -1):
            rmax = max(rmax, height[i + 1])
            right[i] = rmax
        
        res = 0
        for i in range(len(height)):
            res += max(min(left[i], right[i]) - height[i], 0)
        
        return res