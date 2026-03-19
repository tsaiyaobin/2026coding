# week04-4b.py (重寫week04-3.py)
# Leetcode3866. First Unique Even Element
# 老師解法(查陣列)
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = [0] * 200
        for nn in nums:
            H[nn] += 1
        for nn in nums:
            if nn % 2 == 0 and H[nn] == 1:
                return nn 