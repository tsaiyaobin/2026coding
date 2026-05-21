# week13-1.py 學習計劃 graph - BFS 第一題
# Leetcode 1926. Nearest Exit from Entrance in Maze
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([[entrance[0], entrance[1], 0]])
        visited = set()
        visited.add((entrance[0], entrance[1]))
        n = len(maze)
        m = len(maze[0])
        min_step = float('inf')
        while queue:
            x, y, step = queue.popleft() 
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < n and 0 <= new_y < m and (new_x, new_y) not in visited and maze[new_x][new_y] != '+' :
                    visited.add((new_x, new_y))
                    queue.append([new_x, new_y, step + 1])
                    if new_x == 0 or new_x == (n - 1) or new_y == 0 or new_y == (m - 1):
                        return step + 1      
        return -1
