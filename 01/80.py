'''
Remove Duplicates from Sorted Array II
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5,
 with the first five elements of nums being 1, 1, 2, 2 and 3.
 It doesn't matter what you leave beyond the new length.


'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dict = {}
        for i in reversed(range(len(nums))):
            n = nums[i]
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1
            if dict[n] > 2:
                nums.remove(n)
nums = [1,1,1,2]
s = Solution()
s.removeDuplicates(nums)
print(nums)