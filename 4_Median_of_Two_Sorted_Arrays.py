"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #交叉找较小值
        min1, min2 = 0, 0
        i, j = 0, 0
        length = len(nums1) + len(nums2)

        while i + j != length // 2 + 1:
            if i < len(nums1) and j < len(nums2):

                if nums1[i] < nums2[j]:
                    min2 = min1
                    min1 = nums1[i]
                    i += 1
                else:
                    min2 = min1
                    min1 = nums2[j]
                    j += 1
            else:
                if i < len(nums1):
                    min2 = min1
                    min1 = nums1[i]
                    i += 1
                else:
                    min2 = min1
                    min1 = nums2[j]
                    j += 1
        if length % 2 != 0:
            return min1
        else:
            return (min1 + min2) / 2

Solution.findMedianSortedArrays([1], [3, 4])


