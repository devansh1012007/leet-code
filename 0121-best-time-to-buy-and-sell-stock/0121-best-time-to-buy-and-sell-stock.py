# Impt rules :
'''
- don't look for max until a min is decided 
- i_max need to be grater then i_min
- num_max need to graeater then num_min
- Use DP to keep track of the prev best max and min prizes and also to keep track of other possible trades
'''
# ez solution : 
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        maximum = 0
        if length == 1 : return 0
        i = 0
        while i <length:
            j=i+1
            while j < length: 
                if prices[j] > prices[i]:
                    diff = prices[j]-prices[i]
                    if maximum < diff: maximum = diff
                j += 1
            i += 1 
        return maximum
'''
# trying more efficent solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        #if length == 1: return 0 
        min_ = float(inf)
        max_ = float(-inf)
        max_pos = None
        min_pos = None
        #DP=[]
        #DP.append(diff)
        ans = 0
        for num in range(length):
            val = prices[num]
            if val > max_ and val < min_: max_pos, min_pos, max_, min_ = num, num, val, val 
            elif val >= max_ : max_,max_pos = val, num
            elif val <= min_ and num > max_pos : min_, max_, min_pos, max_pos = val, val , num, num
            diff = max_- min_
            if diff > ans: ans = diff
        return ans
        # how the fuck do i re discover the Kadane's Algorithm and use that ? IDK what it is and how to use it but the point is how do i save states such that i can use that information to decide weather i need to switch the max_ and min_ for biggest difference 
        # see the end of maths notes to checkout the re discovered version 
        