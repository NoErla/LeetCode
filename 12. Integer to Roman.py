"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        """
        num = str(num)[::-1]
        result = ""
        list_roman = [["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                      ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                      ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                      ["M", "MM", "MMM"]]
        for index, n in enumerate(num):
            if n == '0':
                continue
            result = list_roman[index][int(n) - 1] + result
        return result

        """
        M = ['', 'M', 'MM', 'MMM']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        return M[num // 1000] + C[num % 1000 // 100] + X[num % 100 // 10] + I[num % 10]


s = Solution()
print(s.intToRoman(400))
