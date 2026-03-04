# Leetcode 1404. Number of Steps to Reduce a Number in Binary Representation to One
class Solution:
    def numSteps(self, s: str) -> int:
        step = 0
        if s == '1':
            return 0
            
        num = int(s, 2)
        while True:            
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
            step += 1
            if num == 1:
                break
        return step