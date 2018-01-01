"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""


class Solution:
    """
    从后往前进行正则匹配
    """
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s = s[::-1]
        p = p[::-1]
        for index, char in enumerate(p):
            if char == ".":
                s = s[1:]
            elif char == "*":
                pass
            else:
                if char != s[0]:
                    return False
                else:
                    s = s[1:]


s = Solution()
a = s.isMatch("ab", ".*b*c*")
print(a)