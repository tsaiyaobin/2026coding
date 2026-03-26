# week05-3.py 學習計畫 Hash Table (Map/set)
# Leetcode 1207. Unique Number of Occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        unique = set()
        for _, value in count.items():
            if value not in unique:
                unique.add(value)
            else:
                return False
        return True