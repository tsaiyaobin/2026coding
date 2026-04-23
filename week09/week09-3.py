# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# week09-3.py 學習計畫 Linked List 第 3 題
# Leetcode 206. Reverse Linked List
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        l = head
        m = l.next
        r = m.next
        l.next = None
        while m is not None:
            m.next = l
            l = m
            m = r
            if r:
                r = r.next
            head = l
        return head