import re
class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'[^a-zA-Z0-9]','', s)# remove all the symbols and spaces
        s = s.lower()
        i = 0
        j = len(s)-1
        # 2 pointer in a loop
        while j>=i:
            if s[i] == s[j]:
                i +=1 
                j -= 1
            else:
                return False
        return True