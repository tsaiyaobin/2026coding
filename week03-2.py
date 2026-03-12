# week03-2.py 學習計畫 Sliding Window 第1題
# Leetcode 643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums)     
        count = sum(nums[0:k]) # 加總前k項
        max_count = count 
        for i in range(k, N):
            count = count + nums[i] - nums [i-k] # 往右擴一格，往左縮一格
            max_count = max(max_count, count)
        return max_count / k