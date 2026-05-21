# week13-4.py 學習計劃 heap 第2題
# Leetcode 2336. Smallest Number in Infinite Set
class SmallestInfiniteSet:
    def __init__(self):
        self.heap = []
        self.added = set()
        self.current = 1

    def popSmallest(self) -> int:
        if self.heap and self.heap[0] < self.current:
            val = heapq.heappop(self.heap)
            self.added.remove(val)
            return val
        val = self.current
        self.current += 1
        return val

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)
            