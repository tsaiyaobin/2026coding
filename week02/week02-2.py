# week02-2.py 學習計畫 Two Points 第1題
# Leetcode 283. Move Zeroes
# 一層迴圈裏面有2個Index，叫做 two points
# Method 1 (老師的解法)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = 0
        for i in range(N):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for i in range(k, N):
            nums[i] = 0

# Method 2 (我的解法，想法來自插入排序)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            up = nums[i]
            j = i
            while j > 0:
                if nums[j-1] == 0:
                    nums[j] = nums[j-1]
                    j -= 1
                else:
                    break
            nums[j] = up

