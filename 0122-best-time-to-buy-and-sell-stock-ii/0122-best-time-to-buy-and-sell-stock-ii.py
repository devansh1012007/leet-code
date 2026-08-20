class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        total = 0
        for i in prices:  
            if (diff := i-prev) > 0:
                total += diff
            prev = i
        return total