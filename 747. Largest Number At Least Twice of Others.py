class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        max_num = nums[0]
        max_num_index = 0
        second_num = max_num
        for index, num in enumerate(nums):
            if num > max_num:
                second_num = max_num
                max_num = num
                max_num_index = index
            else:
                if num > second_num:
                    second_num = num

        if max_num == second_num:
            return 0
        if max_num >= second_num * 2:
            return max_num_index
        else:
            return -1


s = Solution()
print(s.dominantIndex([1, 0]))