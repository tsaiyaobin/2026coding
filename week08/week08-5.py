# week08-5.py 學習計畫 Binary Search 第 3 題
# Leetcode 162. Find Peak Element
# 找到比左右鄰居大的
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0
        for i in range(N):
            if i == 0 and nums[i] > nums[i+1]:
                return i
            elif i == N-1 and nums[i] > nums[i-1]:
                return i
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i