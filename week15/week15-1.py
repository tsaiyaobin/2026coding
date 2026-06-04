# week 15-1a.py 學習計劃 DP-Multidimention 第一題
# LeetCode 62. Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(i, j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            return dp(i-1, j) + dp(i, j-1)
        return dp(m-1, n-1) 

# week 15-1b.py 學習計劃 DP-Multidimention 第一題
# LeetCode 62. Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]