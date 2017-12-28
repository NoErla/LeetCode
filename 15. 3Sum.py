"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    #控制在O(N2)
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def twoSum(nums, target):
            result = []
            dict = {}
            for index, j in enumerate(nums):
                if target == -2 and j == 2:
                    pass
                if target - j in dict:
                    k = [target - j, j]
                    if k not in result:
                        result.append(k)
                dict[j] = index
            return result

        nums.sort()
        result = {}
        result2 = []
        if len(nums) < 3:
            return []
        while len(nums) >= 3:
            one = nums.pop()
            if one not in result:
                proxy = twoSum(nums, 0 - one)
                if proxy:
                        result[one] = proxy
                        for p in proxy:
                            result2.append([one, p[0], p[1]])
        return result2





s = Solution()
print(s.threeSum([0,0,0,0]))