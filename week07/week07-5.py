# week07-5.py 學習計畫 queue 第 1 題
# Leetcode 933. Number of Recent Calls
class RecentCounter:
    # 回傳 3000 毫秒內被ping了幾次
    def __init__(self):
        self.requests = deque([])

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

