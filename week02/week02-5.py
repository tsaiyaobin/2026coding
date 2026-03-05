# week02-4.py 學習計畫 Two Points 第4題
# LeetCode 1679. Max Number of K-Sum Pairs
# 希望能從nums找到兩個數字能相加 = k，共幾組?
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort() # 先從小排到大
        i = 0
        j = len(nums) - 1
        ans = 0
        while i < j:
            if nums[i] + nums[j] == k: 
                ans += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        return ans