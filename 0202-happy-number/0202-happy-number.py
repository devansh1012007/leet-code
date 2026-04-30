class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_num(n):
            output = 0
            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            return output
        j = get_num(n)
        i = j
        j = get_num(j)
        while j != i:
            j = get_num(j)
            j = get_num(j)
            i = get_num(i)
        if i == 1:
            return True
        else: return False    