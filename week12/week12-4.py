# week12-3.py 學習計畫 Graph - DFS 第三題
# Leetcode 1466. Reorder Routes to Make All Paths Lead to the City Zero
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:         
        self.count = 0
        def dfs(city):
            visited[city] = True
            for neighbor, direction in graph[city]:
                if visited[neighbor] != True:
                    self.count += direction
                    dfs(neighbor)

        graph = [[] for _ in range(n)]
        for start, end in connections:
            graph[start].append((end, 1))
            graph[end].append((start, 0))
        visited = [False] * n
        dfs(0)
        return self.count 