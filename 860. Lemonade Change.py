class Solution(object):
    def lemonadeChange(self, bills):
        five = 0
        tens = 0
        twentys = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:         
                five -= 1
                tens += 1
            else:
                tens -= 1
                five -= 1
                twentys += 1
                if tens < 0 and five > 1 :
                    five -= 2
                    tens += 1
            if five< 0 or tens< 0 or twentys< 0:
                return False  

        return True if five>= 0 and tens>= 0 and twentys>= 0 else False

#######     wont work
class Solution(object):
    def lemonadeChange(self, bills):
        nums = [0,0,0]
        for i in bills:
            if i == 5:
                nums = nums + [1,0,0]
            elif i == 10:
                nums = nums + [-1,1,0]         
            else:
                nums = nums + [-1,-1,1] 
                if nums[1] < 0 and nums[0] > 1 :
                    nums = nums + [-2,1,0]

            if nums[0]< 0 or nums[1]< 0 or nums[2]< 0:
                return False  

        return True 

