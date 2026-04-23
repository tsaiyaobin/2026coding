# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# week09-6.py 學習計畫 Linked List 第 2 題
# Leetcode 328. Odd Even Linked List
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        odd = head
        even = head.next
        dummy = even
        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = dummy
        return head
            