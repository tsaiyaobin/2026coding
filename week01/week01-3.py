# week01-3.py 學習計畫 Array/String 第2題
# 1071. Greatest Common Divisor of Strings
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        N = gcd(len(str1), len(str2))
        return str1[:N]