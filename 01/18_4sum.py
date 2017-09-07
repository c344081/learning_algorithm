'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
class Solution(object):
    def findNums(self, nums, target, N, result, results):
        if N < 2 or len(nums) < N or nums[0] * N > target or nums[-1] * N < target:
            return
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        else:
            for i in range(len(nums) - N + 1):
                if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                    self.findNums(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        self.findNums(sorted(nums), target, 4, [], results)
        return results

nums = [1, 0, -1, 0, -2, 2]
solution = Solution()
results = solution.fourSum(nums, 0)
print(results)
