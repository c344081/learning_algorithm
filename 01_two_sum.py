# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return None
        if len(nums) < 2: return None
        dict = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in dict:
                return dict[y], i
            else:
                dict[x] = i

nums = [1, 2, 3, 5, -8, 0, 7]
s = Solution()
t = s.twoSum(nums, 4)
print(t)