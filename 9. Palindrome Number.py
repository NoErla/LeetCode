"""
Determine whether an integer is a palindrome. Do this without extra space.
"""


class Solution:
    @staticmethod
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x is not 0):
            return False

        # stop loop when reverseNum bigger than cutted x
        reverseNum = 0
        while x > reverseNum:
            reverseNum = reverseNum * 10 + (x % 10)
            x = x // 10  # floor division // instead of /

        # odd or even digit situation, doesn't matter
        return reverseNum == x or x == reverseNum // 10  # floor division // instead of /

Solution.isPalindrome(0)
