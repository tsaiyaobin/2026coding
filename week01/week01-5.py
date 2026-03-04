# week01-5.py 學習計畫 Array/String 第7題
# Leetcode 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postsum = [1]
        presum = [1]
        N = len(nums)
        for i in range(N):
            presum.append(nums[i] * presum[-1])
            postsum.append(nums[N-i-1] * postsum[-1])
        ans = []
        for j in range(N):
            ans.append(presum[j] * postsum[N-j-1])
        return ans