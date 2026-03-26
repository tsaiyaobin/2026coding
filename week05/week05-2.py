# week05-2a.py 學習計畫 Hash Table (Map/set) 最爛版本
# Leetcode 2215. Find the Difference of Two Arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1= []
        for num in nums1:
            if num not in nums2:
                ans1.append(num)
        ans2= []
        for num in nums2:
            if num not in nums1:
                ans2.append(num)
        return [list(set(ans1)), list(set(ans2))]
        
# week05-2b.py 學習計畫 Hash Table (Map/set) 版本二
# Leetcode 2215. Find the Difference of Two Arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        ans1= []
        for num in nums1:
            if num not in nums2:
                ans1.append(num)
        ans2= []
        for num in nums2:
            if num not in nums1:
                ans2.append(num)
        return [list(ans1), list(ans2)] 

# week05-2c.py 學習計畫 Hash Table (Map/set) 版本三
# Leetcode 2215. Find the Difference of Two Arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:     
        s_nums1 = set(nums1)
        s_nums2 = set(nums2)
        ans = []
        ans.append(list(s_nums1 - s_nums2))
        ans.append(list(s_nums2 - s_nums1))
        return ans        