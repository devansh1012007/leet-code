class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        total = 0
        for i in prices:
            '''
                if prev == i: 
                    continue 
            '''    
            if (diff := i-prev) > 0:
                total += diff
            prev = i
        return total
        '''
            if prev == i: 
                continue 
        '''
        '''ans = 0
        add=False
        profit=0
        max_, min_ = prices[0],prices[0]   
        for val in prices:
            if val >= max_ : max_= val
            elif val <= min_ : 
                min_, max_ = val, val
                add = True
            diff = max_ - min_
            if diff > ans: 
                ans = diff
                if add :profit,add = ans+profit, False
        return profit'''