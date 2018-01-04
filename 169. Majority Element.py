"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_num = nums.pop()
        count = 1
        while nums:
            num = nums.pop()
            if num != majority_num:
                if count > 0:
                    count -= 1
                else:
                    majority_num = num
                    count = 1
            else:
                count += 1
        return majority_num

s = Solution()
print(s.majorityElement([2,2,2,1,1]))
