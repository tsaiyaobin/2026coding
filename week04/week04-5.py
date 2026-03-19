# week04-5.py 學習計畫 Prefix Sum 第2題
# Leetcode724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [0]
        right_sum = [0]
        N = len(nums)
        for i in range(N): # 從左加到右，以及從右加到左
            left_sum.append(nums[i] + left_sum[-1])
            right_sum.append(nums[N-i-1] + right_sum[-1])
        right_sum = list(reversed(right_sum))
        for i in range(1, N + 1):
            if left_sum[i-1] == right_sum[i]: # 觀察哪一個 index 的 左邊加總 = 右邊加總
                return i-1 # 有找到就回傳 nums 的 index
        return -1