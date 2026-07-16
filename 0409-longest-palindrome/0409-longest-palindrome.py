class Solution:
    '''
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
    '''
    def longestPalindrome(self, s: str) -> int:
        char = {}
        length = 0
        odd_count = 0
        for i in s: char[i] = char.get(i,0)+1
        for i in char.values():
            if i%2==0:length +=i
            else : 
                length +=(i-1)
                odd_count+=1
        if odd_count>0:length += 1
        return length