class Solution:
    @staticmethod
    def myAtoi(str):
        """
        :type str: str
        :rtype: int
        """
        try:
            if len(str) == 0:
                return 0
            str = str.strip()
            if len(str) == 0:
                if not str[0].isdigit():
                    return 0

            sign = -1 if str[0] == "-" else 1
            if str[0] in ["-", "+"]:
                str = str[1:]
            if len(str) == 0:
                return 0
            i = 0
            number = ""
            while i < len(str) and str[i].isdigit():
                number += str[i]
                i += 1

            return max(-2 ** 31, min(sign * int(number), 2 ** 31 - 1))
        except:
            return 0

Solution.myAtoi("+-2")