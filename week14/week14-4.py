# week14-4.py 學習計劃 1D DP
# Leetcode 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = [0, 0, 0]
        N = len(nums)
        for i in range(N):
            ans.append(max(nums[i] + ans[-2], nums[i] + ans[-3]))
        return max(ans[-1], ans[-2])