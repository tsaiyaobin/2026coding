# week07-6.py 學習計畫 queue 第 2 題
# Leetcode 649. Dota2 Senate
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))
        counter = Counter(senate)
        R = counter['R']
        D = counter['D']
        ban_R = 0
        ban_D = 0
        while queue:
            now = queue.popleft()
            if now == 'R':
                if ban_R > 0: # 有R被禁止
                    R -= 1 # 少一個人員
                    ban_R -= 1 # 扣掉一個被ban的數量
                    continue
                else:
                    ban_D += 1 # ban對方
                    queue.append(now) # 自己在回去排隊
            else:
                if ban_D > 0: # 有D被禁止
                    D -= 1 # 少一個人員
                    ban_D -= 1 # 扣掉一個被ban的數量
                    continue
                else:
                    ban_R += 1 # ban 對方
                    queue.append(now)
            if R == 0: return 'Dire'
            if D == 0: return 'Radiant'