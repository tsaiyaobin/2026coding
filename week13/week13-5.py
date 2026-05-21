# week13-5.py 學習計劃 heap 第3題
# Leetcode 2542. Maximum Subsequence Score
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr_sort = sorted(zip(nums2, nums1), reverse = True)
        nums2, nums1 = zip(*arr_sort)
        count = 0
        max_count = 0
        heap = []
        for n1, n2 in zip(nums1, nums2):
            heapq.heappush(heap, n1)
            count += n1
            if len(heap) > k:
                count -=  heapq.heappop(heap)
            if len(heap) == k:
                max_count = max(max_count, count * n2)
        return max_count