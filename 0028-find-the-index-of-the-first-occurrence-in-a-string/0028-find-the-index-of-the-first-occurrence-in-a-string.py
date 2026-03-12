class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        i2 = i
        while i < len(haystack) :
            idx = 0
            while i < len(haystack) and haystack[i] == needle[idx] :
                i = i + 1
                idx = idx + 1
                if i - i2 == len(needle) :
                    return i2
            #i = i + 1
            i2 = i2 + 1
            i = i2
            #print("i =", i, "i2 =", i2, haystack[i2])
        return -1
        