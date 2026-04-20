# week08-6.py 學習計畫 Binary Search 第 4 題
# Leetcode 875. Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(k): # 一小時吃k個香蕉, 能在h小時內吃完嗎
            total = 0
            for pile in piles:
                total += pile // k
                if pile % k > 0:
                    total += 1
            return total <= h
        return bisect_left(range(1, max(piles)), True, key = time) + 1 