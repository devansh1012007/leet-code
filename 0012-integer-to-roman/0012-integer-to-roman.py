'''class Solution:
    def intToRoman(self, num: int) -> str:
        # 1st break number into all the numbers at each place in number 
        # 2nd an small converter to do the maths and change the number into sum of simple numbers from hast table
        # 3rd hash table itrates through all the numbers that the engine has output and make a str of romam numbers


        table = {
            1:'I',
            5:'V',
            10:'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M',
        }

        # Breaking down number:
        components = []
        while num >= 0:
            digit = num % 10                # 1. Extract the last digit
            result = [10 * multiplier for x in components]
            components = result
            components.append(digit)
            num = num // 10
        for i in components:
'''
# ---------------------------------------------
# re-start
class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        res = []

        for value, symbol in value_symbols:
            if num == 0:
                break
            count = num // value
            res.append(symbol * count)
            num -= count * value

        return ''.join(res)