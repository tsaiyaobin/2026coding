# week03-3.py 學習計畫 Sliding Window 第3題
# Leetcode 1004. Max Consecutive Ones III
# 可以把 k 個 0 變成 1
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        end = 0
        zero = 0
        for start in range(len(nums)): # 視窗持續往右擴增
            if nums[start] == 0:
                zero += 1
            if zero > k: # 視窗內的0超過限制(k)
                if nums[end] == 0: # 如果最左邊遇到0就吐掉
                    zero -= 1
                end += 1 # 維持目前最大的長度
        return start - end + 1