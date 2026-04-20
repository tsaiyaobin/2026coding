# week08-4.py 學習計畫 Binary Search 第 2 題
# Leetcode 2300. Successful Pairs of Spells and Potions
# 想知某種 spells[i] 魔法, 配給種藥水可以成功
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort() # 藥水小到大排好
        ans = []
        N = len(potions)
        for spell in spells:
            now  = N - bisect_left(potions, success / spell)
            ans.append(now)
        return ans

        """ bisect 用法
        from bisect import bisect_left, bisect_right

        a = [1, 3, 3, 5, 7]

        bisect_left(a, 3)   # 1，第一個 3 的位置
        bisect_right(a, 3)  # 3，最後一個 3 的後面

        bisect_left(a, 4)   # 3，4 應該插在 index 3
        bisect_right(a, 4)  # 3，同上（4 不存在時左右相同）
        """