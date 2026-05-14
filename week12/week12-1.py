# week12-1a.py 學習計畫 Graph - DFS 第一題
# Leetcode 841. Keys and Rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool: 
        def dfs(room_idx, stack):
            visited[room_idx] = True
            for key in rooms[room_idx]:
                if visited[key] == False:
                    stack.append(key)
            if stack:
                room = stack.pop()
                dfs(room, stack)
                    
        N = len(rooms)
        visited = [False] * N
        dfs(0, [])
        if False in visited:
            return False
        else:
            return True 
        
# week12-1b.py 學習計畫 Graph - DFS 第一題
# Leetcode 841. Keys and Rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 第一個房間一定可以開 (index = 0)
        N = len(rooms)
        visited = [False] * N
        visited[0] = True # 拜訪第一間房間
        queue = deque(rooms[0]) 
        while queue:
            key = queue.popleft() # 去有鑰匙的房間
            visited[key] = True
            for keys in rooms[key]:
                if visited[keys] is False: # 走過就無需再走
                    queue.append(keys)

        if False in visited: 
            return False
        else:
            return True
        
        
# week12-1c.py 學習計畫 Graph - DFS 第一題
# Leetcode 841. Keys and Rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool: 
        def dfs(room_idx):
            for key in rooms[room_idx]:
                if visited[key] == False:
                    visited[key] = True
                    dfs(key)

        N = len(rooms)
        visited = [False] * N
        visited[0] = True
        dfs(0)
        if False in visited:
            return False
        else:
            return True 
        