class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        max_ = min_ = prices[0]  
        for val in prices:
            if val >= max_ : max_= val
            elif val <= min_ : min_ = max_ = val
            diff = max_ - min_
            if diff > ans: ans = diff
        return ans
