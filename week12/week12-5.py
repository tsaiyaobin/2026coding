# week12-4.py 學習計畫 Graph - DFS 第四題
# Leetcode 399. Evaluate Division
class Solution:
      def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
          def dfs(start, end):
              if start == end:          # 新增：找到終點，停止
                  self.found = True
                  return
              visited.add(start)
              for node, value in graph[start]:
                  if node not in visited:
                      self.count *= value
                      dfs(node, end)    # 修正：node 而不是 start
                      if self.found:
                          return
                      self.count /= value  # 新增：回溯，此路不通就還原
          N = len(equations)
          graph = defaultdict(list)
          for i in range(N):
              a, b = equations[i]
              value = values[i]
              graph[a].append((b, value))
              graph[b].append((a, 1 / value))
          ans = []
          for start, end in queries:
              if start not in graph or end not in graph:
                  ans.append(-1.0)
              else:
                  visited = set()
                  self.count = 1.0     # 新增：每次查詢前初始化
                  self.found = False   # 新增：記錄是否找到終點
                  dfs(start, end)
                  ans.append(self.count if self.found else -1.0)  # 修正
          return ans