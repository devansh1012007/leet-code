'''def plusOne(digits,i = -1):
        if digits[i] :
            if digits[i] + 1 == 10:
                digits[i] = 0
                plusOne(digits ,i-1)
            digits[i] = digits[i] + 1
        else :
            digits.append(1)
digits=[1,2,2,3]
plusOne(digits)
print(digits)
'''
class Solution(object):
    
    def plusOne(self, digits,i = -1):
        try :
            if digits[i] + 1 == 10:
                digits[i] = 0
                #print(digits)
                self.plusOne(digits ,i-1)## what to do to make the recursion work 
            #digits[i] = digits[i] + 1
        except :
            #print(digits)
            digits.append(0)# not good steps
            #print(digits)
            digits[0] = 1



# calling the class
digits = [9,9,9]
#digits.add(1)
sol = Solution()
sol.plusOne(digits)
print(digits)


# final ----------------------------------------
class Solution(object):
    
    def plusOne(self, digits,i = -1):
        try :
            if digits[i] + 1 == 10:
                digits[i] = 0
                self.plusOne(digits ,i-1)## what to do to make the recursion work ---> done
            else :
                digits[i] = digits[i] + 1
        except :
            digits.append(0)
            digits[0] = 1
        return digits
# for some fucking rason its giving null ----> solved, just add return to it 