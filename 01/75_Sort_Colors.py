'''
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
'''

# 冒泡
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return []
        # records = [0] * 3
        # for n in nums:
        #     records[n] += 1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

class Solution2(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return []
        records = [0] * 3
        for n in nums:
            records[n] += 1
        l = 0
        for i, n in enumerate(records):
            if n > 0:
                for j in range(n):
                    nums[l + j] = i
                l += n

nums = [1, 0, 2, 0]
s = Solution2()
s.sortColors(nums)
print(nums)