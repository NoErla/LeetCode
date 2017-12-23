"""
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution:

    @staticmethod
    def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        str = strs[0]
        i = 1
        while len(str) != 0 and i < len(strs):
            j = 0
            while j < len(str) and j < len(strs[i]):
                if str[j] != strs[i][j]:
                    str = str[:j]
                    break
                j += 1
            else:
                str = str[:j]
            i += 1
        print(str)
        return str

        """
        if not strs:
            return ''
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        return min(strs)
        """


Solution.longestCommonPrefix(["a", "b"])