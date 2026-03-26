# week05-6.py 學習計畫 Hash Table (Map/set)
# Leetcode 2352. Equal Row and Column Pairs
# 我的寫法
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid2 = {}
        N = len(grid)
        count = 0
        for i in grid:
            row = tuple(i)
            if row not in grid2:
                grid2[row] = [1, 0]  # [row數, col數]
            else:
                grid2[row][0] += 1
        for i in range(N):
            col = tuple([row[i] for row in grid])
            if col in grid2:
                grid2[col][1] += 1
        for _, value in grid2.items():
            if value[1] > 0:
                count += value[0] * value[1]  # row數 × col數
        return count
        
# 老師的寫法
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter()
        for row in grid:
            counter[tuple(row)] += 1
        ans = 0
        for col in zip(*grid):
            ans += counter[tuple(col)]

        return ans