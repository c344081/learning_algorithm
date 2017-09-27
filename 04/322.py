"""
Coin Change

You are given coins of different denominations and a total amount of money amount.
 Write a function to compute the fewest number of coins that you need to make up that amount.
 If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""

# 把Solution那篇文章的方法写了一遍...
import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        return DpBottomUpSolution().coinChange(coins, amount)

class BruteForceSolution(object):
    def helper(self, idx, coins, amount):
        if amount == 0:
            return 0
        if amount < 0 or idx >= len(coins):
            return -1

        maxVal = int(amount / coins[idx])
        minCount = sys.maxsize
        for x in range(maxVal + 1):
            if amount >= x * coins[idx]:
                ret = self.helper(idx + 1, coins, amount - x * coins[idx])
                if ret == -1:
                    continue
                minCount = min(minCount, ret + x)
        return -1 if minCount == sys.maxsize else minCount

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        return self.helper(0, coins, amount)

class DpTopDownSolution(object):
    # F(S) = min(F(S−ci)) + 1
    def helper(self, coins, remain, counts):
        if remain < 0:
            return -1
        if remain == 0:
            return 0
        if counts[remain - 1] != 0:
            return counts[remain - 1]
        minCount = sys.maxsize
        for coin in coins:
            ret = self.helper(coins, remain - coin, counts)
            if ret < 0 or ret >= minCount:
                continue
            minCount = ret + 1
        counts[remain - 1] = -1 if minCount == sys.maxsize else minCount
        return counts[remain - 1]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        if amount < 1:
            return 0
        return self.helper(coins, amount, [0] * amount)


class DpBottomUpSolution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return -1 if dp[amount] > amount else dp[amount]


s = Solution()
minCount = s.coinChange([3, 9, 400, 380], 8888)
print(minCount)
