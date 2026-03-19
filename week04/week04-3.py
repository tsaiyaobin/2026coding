# week04-3.py 學習計畫 Prefix Sum 第2題
# Leetcode3866. First Unique Even Element
# 我的解法(查字典)
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        even = []
        d = {}
        for i in range(len(nums)): # 紀錄偶數出現的次數
            if nums[i] % 2 == 0 and nums[i] not in d:
                d[nums[i]] = 1
            elif nums[i] % 2 == 0 and nums[i] in d:
                d[nums[i]] += 1
        for j in range(len(nums)): # 第一個偶數且只有出現過一次，就直接輸出
            if nums[j] in d and d[nums[j]] == 1:
                return nums[j]
        return -1 
# 我的解法 Count記數
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        count = Counter(nums)
        for i in range(len(nums)): # 第一個偶數且只有出現過一次，就直接輸出
            if nums[i] % 2 == 0 and count[nums[i]] == 1:
                return nums[i]
        return -1        
# 老師解法(查陣列)
    class Solution:
        def firstUniqueEven(self, nums: list[int]) -> int:
            N = len(nums)
            H = [0] * 200
            for i in range(N):
                H[nums[i]] += 1
            for i in range(N):
                if nums[i] % 2 == 0 and H[nums[i]] == 1:
                    return nums[i]
            return -1