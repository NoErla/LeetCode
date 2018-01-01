"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution:

    @staticmethod
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        """
        遍历字符串的方法，很蠢
        max_length = 0

        for index, char in enumerate(s):
            if len(s) - index < max_length:
                break
            end = index + max_length + 1
            if len(s[index:end]) > len(set(s[index:end])):
                continue
            str = s[index:end]
            if len(s[end:]) == 0:
                if len(str) > max_length:
                    max_length = len(str)
                continue
            for char2 in s[end:]:
                if char2 not in str:
                    str += char2
                    if len(str) > max_length:
                        max_length = len(str)
                else:
                    if len(str) > max_length:
                        max_length = len(str)
                    break

        print(max_length)
        return max_length
        """

        left, max_length, right = 0, 0, 0
        str = ""
        for right in range(len(s)):
            if s[right] not in str:
                str += s[right]
                if len(str) > max_length:
                    max_length = len(str)
            else:
                #删除重复字符之前的字符
                str += s[right]
                str = str[str.index(s[right]) + 1:]
                left += 1
        print(max_length)
        return max_length
Solution.lengthOfLongestSubstring("dvdf")
#aab dvdf pwwkew