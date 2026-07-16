class Solution:
    def longestPalindrome(self, s: str) -> int:
        #if len(str) == 0 : return 0
        char = []
        length = 0
        for i in s:
            if i not in char: char.append(i)
            else: 
                char.remove(i)
                length += 2
        if len(char) >0:length += 1
        return length