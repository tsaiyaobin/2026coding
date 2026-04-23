# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# week09-7.py 學習計畫 Linked List 第 4 題
# Leetcode 2130. Maximum Twin Sum of a Linked List
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = []
        while head is not None:
            ans.append(head.val)
            head = head.next
        N = len(ans)
        max_count = 0
        for i in range(N//2):
            max_count = max(max_count, ans[i] + ans[N-i-1])
        return max_count