# week02-3.py 學習計畫 Two Points 第2題
# LeetCode 392. Is Subsequence
# 一層迴圈裏面有2個Index，叫做 two points
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        j = 0
        for i in range(len(t)):
            if s[j] == t[i]:
                j += 1
            if j == len(s):
                return True
        return False