"""
House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
 determine the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution(object):

    # |               n = 0, f0 = a[0]
    # |--|            n = 1 f1 = max(0 + a[1], f0)
    # |--|--|         n = 2 f2 = max(f0 + a[2], f1)
    # |--|--|--|      n = 3 f3 = max(f1 + a[3], f2)

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = len(nums)
        if count == 1:
            return nums[0]
        m1, m2 = 0, nums[0]

        for i in range(1, len(nums)):
            m2 = nums[i] + m1
            m1 = max(m1, m2)
        return max(m1, m2)

        i = 1,  m2 = nums[1], m1 = max(nums[0], nums[1])
        i = 2, m2 = nums[2] + f1  m1 = f1, nums[2] + f1




