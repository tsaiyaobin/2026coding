# week13-2.py 學習計劃 graph - BFS 第二題
# Leetcode 994. Rotting Oranges
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append([i, j, 0])
        count = 0
        while queue:
            for _ in range(len(queue)):
                x, y, step = queue.popleft()
                for dx, dy in direction:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 1:
                        queue.append([new_x, new_y, step + 1])
                        grid[new_x][new_y] = 2
            count = step
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return count