# week01-2.py 學習計畫 Array/String 第1題
# Leetcode 1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        N1 = len(word1)
        N2 = len(word2)
        new = ""
        N = min(N1, N2) # 選最短的長度，不然短的字串沒有index會跳Error
        for i in range(N):
            new += word1[i] + word2[i]
        new += word1[N2:] # 把剩下的加完
        new += word2[N1:] # 把剩下的加完
        return new
            