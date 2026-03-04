# week01-4.py 學習計畫 Array/String 第3題
# Leetcode 1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        arr = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                arr[i] = True
        return arr