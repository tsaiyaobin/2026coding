# week03-2.py 學習計畫 Sliding Window 第2題
# 1456. Maximum Number of Vowels in a Substring of Given Length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = set("aeiou")
        count = 0
        print(vow)
        for i in range(k): # 初始化視窗
            print(s[i])
            if s[i] in vow:
                count += 1
        max_count = count
        for j in range(k, len(s)): # 往右擴一格，往左縮一格
            if s[j-k] in vow:
                count -= 1
            if s[j] in vow:
                count += 1
            if max_count < count:
                max_count = count
        return max_count