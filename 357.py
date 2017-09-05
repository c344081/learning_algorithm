'''
Count Numbers with Unique Digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91.
(The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

'''
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def countNumbers(n):
            if n == 0: return 1
            if n == 1: return 10
        if n > 1:
            ret, s = 10, 9 # s为最高位的可能数字数量
            for i in range(1, n):
                s *= (9 - i + 1)
                ret += s
        return ret
n = 2
s = Solution()
print(s.countNumbersWithUniqueDigits(n))
