# week 15-4a.py 學習計劃 DP-Multidimention 第四題
# LeetCode 72. Edit Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = []
        for i in range(n + 2):
            dp.append([])
            for j in range(m + 2):
                dp[i].append(0)
        for i in range(1, n + 1):
            dp[i][0] = i
        for j in range(1, m + 1):
            dp[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[n][m]

# week 15-4b.py 學習計劃 DP-Multidimention 第四題
# LeetCode 72. Edit Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if word1[i] == word2[j]:
                return dp(i-1, j-1)
            else:
                return min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1
        return dp(len(word1)-1, len(word2)-1)