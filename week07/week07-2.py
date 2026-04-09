# week07-2.py 學習計畫 Stack 第 2 題目
# Leetcode 735. Asteroid Collision
# 有很多不同體積的行星，正號是往右，負號往左。如果發生相撞，體積小的會毀掉，體積一樣則一起毀掉。
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            while ans != [] and a < 0: # 遇到往左的行星
                if ans[-1] > 0 and abs(a) < ans[-1]: # 往右的行星 > 往左的行星
                    break
                elif ans[-1] > 0 and abs(a) == ans[-1]: # 往右的行星 = 往左的行星
                    ans.pop() # 往左、往右都爆炸，所以pop往右的
                    break # 往左不會append
                elif ans[-1] > 0 and abs(a) > ans[-1]: # 往右的行星 < 往左的行星
                    ans.pop()
                else:
                    ans.append(a)
                    break
            else:
                ans.append(a)
        return ans