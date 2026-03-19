# week04-4a.py 學習計畫 Prefix Sum 第1題
# Leetcode 1732. Find the Highest Altitude
# 找到最高的海拔高度(highest_altitude)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = H = 0
        for gg in gain:
            H += gg
            ans = max(ans, H)
        return ans