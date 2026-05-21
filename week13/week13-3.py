# week13-3.py 學習計劃 heap 第2題
# Leetcode 994. Rotting Oranges
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        N = len(nums)
        for i in range(k):
            heapq.heappush(heap, nums[i])
        for i in range(k, N):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        return heap[-k] 


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for _ in range(len(nums) - k):
            heappop(nums)
        return nums[0]