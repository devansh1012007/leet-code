
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = float(inf)
        max_ = float(-inf)
        ans = 0
        for val in prices:
            if val > max_ and val < min_: max_, min_ = val, val 
            elif val >= max_ : max_= val
            elif val <= min_ : min_, max_ = val, val
            diff = max_ - min_
            if diff > ans: ans = diff
        return ans
