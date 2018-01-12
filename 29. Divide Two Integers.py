"""
 Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        flag = - 1 if dividend * divisor < 0 else 1
        i = 0
        divisor = abs(divisor)
        dividend = abs(dividend)
        while divisor <= dividend:
            i += 1
            divisor = divisor << 1
        else:
            divisor = divisor >> 1
            i -= 1
        result = 0
        while i >= 0:
            if dividend >= divisor:
                dividend -= divisor
                result += 2 ** i
            divisor = divisor >> 1
            i -= 1

        if result * flag <= -2147483648:
            return -2147483648
        if result * flag >= 2147483647:
            return 2147483647
        return result * flag



s = Solution()
print(s.divide(-1, -1))

