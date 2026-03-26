# week05-5.py 學習計畫 Hash Table (Map/set)
# Leetcode 1207. Unique Number of Occurrences
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 給兩個字串，可以交換兩個字元的位置，也可以將所有字元換成字串中的另一個字元
        # 若經過以上兩個條件可以使word1 == word2就回傳true
        N1, N2 = len(word1), len(word2)
        if N1 != N2: # 字串長度不一樣直接回傳FALSE
            return False
        count1, count2 = Counter(word1), Counter(word2) # 計算每個字元出現的次數
        ans1, ans2 = [], []
        element1, element2 = set(), set() # 存放出現那些字元
        for key1, value1 in count1.items():
            ans1.append(value1)
            element1.add(key1)
        for key2, value2 in count2.items():
            ans2.append(value2)
            element2.add(key2)
        ans1.sort()
        ans2.sort()
        if ans1 == ans2 and element1 == element2:
            return True
        return False