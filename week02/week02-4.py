# week02-4.py 學習計畫 Two Points 第3題
# LeetCode 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        j = len(height) - 1
        max_area = 0
        i = 0
        while i < j:
            count = (j - i) * min(height[j], height[i]) # 算目前的面積
            if height[j] > height[i]: # 如果height[j] > height[i]，i就往右走
                i += 1
            else:
                j -= 1
            max_area = max(max_area, count) # 更新最大面積
        return max_area
            