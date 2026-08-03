# Rules : 
'''
if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
# comparing and saving states at each step. 
Its we have to make something like a DFS but at each step we need to compare sum of steps till now with the other possible past and take the lowest path 
'''
# lets make V1 first 
#class Solution:
'''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 1st initailizing i
        curr_sum = 0
        prev_num = 0
        i_prev = 0
        dp=[]
        # Think about simplicity and  nobility 
        for row in triangle:
            for num in range(len(row)-1):
                if num == i_prev : 
                    number = row[num]
                    dp.append(number)
                    if number 
                    i_prev = num
                elif num == i_prev+1:
                    dp.append(row[num])
                    i_prev = num
            prev_num =  
'''
# V2 tring to Think about simplicity and  nobility 
'''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        length = len(triangle)
        top = triangle[0].pop()
        if length == 1:
            return top
        DP = []# can't understant or realize how to revert back and explore other paths & how to use DP for that 
        self.recursive(top, i= 0, triangle, )
'''
# v3 re-visualize or transorm the inital state or problems into making it simpler
# so basically my prev approch or intuition is right but didn't figure out dp but after a bit of hints (not chating) i got it how 
# this algo it optimised by choosing the favoured option in conflicting position -- whyu ? 
# # cause the ocally optimal soultion is actually considering all the previous decionas + better solution 

# how do i identify the common pos in the layer under to take the best path 

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        DP = []
        for row in triangle:
            new_DP = []
            length = len(row)
            if length>1:
                new_DP.append((row[0]+DP[0]))
                for i in range(1,length-1):
                    new_DP.append(min((row[i]+DP[i]),(row[i]+DP[i-1])))
                
                new_DP.append((row[-1]+DP[-1]))
            else:new_DP.append(row.pop())
            DP=new_DP
        return min(DP)