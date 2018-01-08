"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def cartesian_product(arr1, arr2):
            list = []
            if len(arr1) == 0:
                return arr2
            if len(arr2) == 0:
                return arr1
            for str1 in arr1:
                for str2 in arr2:
                    list.append(str1 + str2)
            return list
        dict = {}
        dict['0'] = []
        dict['1'] = []
        dict['2'] = ['a', 'b', 'c']
        dict['3'] = ['d', 'e', 'f']
        dict['4'] = ['g', 'h', 'i']
        dict['5'] = ['j', 'k', 'l']
        dict['6'] = ['m', 'n', 'o']
        dict['7'] = ['p', 'q', 'r', 's']
        dict['8'] = ['t', 'u', 'v']
        dict['9'] = ['w', 'x', 'y', 'z']
        result = []

        for i in digits:
            result = cartesian_product(result, dict[i])
        return result



s = Solution()
print(s.letterCombinations(""))