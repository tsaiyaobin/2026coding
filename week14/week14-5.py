# week14-5.py 學習計劃 1D DP
# Leetcode 790. Domino and Tromino Tiling
class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1, 1, 2, 5]
        if n <= 3:
            return dp[n]
        for i in range(4, n+1):
            dp.append(2*dp[i-1] + dp[i-3])
        return dp[-1] % (10**9 + 7)