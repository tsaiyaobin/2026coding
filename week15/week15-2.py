# week 15-2a.py 學習計劃 DP-Multidimention 第二題
# LeetCode 1143. Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dp(i-1, j-1) + 1
            else:
                return max(dp(i-1, j), dp(i, j-1))
        return dp(len(text1)-1, len(text2)-1)
# week 15-2b.py 學習計劃 DP-Multidimention 第二題
# LeetCode 1143. Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = []
        for i in range(n+2):
            dp.append([])
            for j in range(m+2):
                dp[i].append(0)
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-2][-2]
