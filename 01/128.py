'''
Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 0: return 0

        curLength = 1
        maxLength = 1
        records = {}
        for i in range(len(nums)):
            n = nums[i]
            if n not in records:
                records[n] = 1
            else:
                records[n] = records[n] + 1
        pre = 0
        for i, n in enumerate(sorted(records)):
            if n == pre + 1 and i > 0:
                curLength += 1
            else:
                curLength = 1
            pre = n
            maxLength = max(maxLength, curLength)
        return maxLength

nums = [100, 4, 200, 1, 3, 2]
s = Solution()
print(s.longestConsecutive(nums))