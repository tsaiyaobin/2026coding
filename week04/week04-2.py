# week04-2.py 學習計畫 Prefix Sum 第1題
# Leetcode 1732. Find the Highest Altitude
# 找到最高的海拔高度(highest_altitude)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        dp = [0]
        highest_altitude = dp[-1]
        for i in range(n):
            dp.append(dp[-1] + gain[i]) # 逐個累加
            if dp[-1] > highest_altitude:
                highest_altitude = dp[-1]
        return highest_altitude