# week07-3.py 學習計畫 Stack 第 1 題目
# Leetcode 2390. Removing Stars From a String
class Solution:
    def removeStars(self, ss: str) -> str:
        ans = []
        for s in ss:
            if s == '*':
                ans.pop()
            else:
                ans.append(s)
        return ''.join(ans)
        