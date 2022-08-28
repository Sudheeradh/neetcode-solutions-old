class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            ind = -1
            while stack and stack[-1][0] > heights[i]:
                val, ind = stack.pop()
                maxArea = max(maxArea, (i-ind)*val)
            stack.append([heights[i], i if ind == -1 else ind])
            
        while stack:
            val, ind = stack.pop()
            maxArea = max(maxArea, val * (len(heights) - ind))
        
        return maxArea
                