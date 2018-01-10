"""
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    #卡特兰数
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * n:  #括号全部用完
                ans.append(S)
                return
            if left < n:#左括号还没用完可直接打印
                backtrack(S + '(', left + 1, right)
            if right < left:#右括号要比左括号数量少的情况下才能打印
                backtrack(S + ')', left, right + 1)
        backtrack()
        return ans


s = Solution()
print(s.generateParenthesis(2))