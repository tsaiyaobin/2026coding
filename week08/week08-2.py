# week08-2.py 學習計畫 Binary Search 第 1 題
# Leetcode 374. Guess Number Higher or Lower
# 給 guess() 你可以呼叫他，找出1.....n裡面的答案
class Solution:
    def guessNumber(self, n: int) -> int:
        # 方法一
        return bisect_left(range(n+1), 0, key = lambda x: -guess(x))

        # 每次猜一半
        # 方法二
        left, right = 1, n # 左右範圍
        while left < right:
            mid = (left + right) // 2 # 猜中間的數字
            if guess(mid) == 0 : # 猜中數字
                return mid
            elif guess(mid) == 1: # 暗示你要高一點(中間改為下界)
                left = mid + 1 
            else: # 暗示你要低一點(中間改為上界)
                right = mid 
        return left 
        
            


