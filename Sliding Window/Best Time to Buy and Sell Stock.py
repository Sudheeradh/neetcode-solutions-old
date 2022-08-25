class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0
        while (r < len(prices)):
            diff = prices[r] - prices[l]
            maxP = max(maxP, diff)
            if (diff < 0):
                l = r
                r += 1
            else:
                r += 1
        return maxP