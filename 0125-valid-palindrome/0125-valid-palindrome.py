import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]','', s)
        s = s.lower()
        print(s)
        i = 0
        j = len(s)-1
        while j>=i:
            if s[i] == s[j]:
                i +=1 
                j -= 1
            else:
                return False
        return True