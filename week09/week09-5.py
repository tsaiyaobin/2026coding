# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# week09-5.py 學習計畫 Linked List 第 1 題
# Leetcode 2095. Delete the Middle Node of a Linked List
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        once = ListNode(0) # 一次走一格
        once.next = head
        twice = head # 一次走兩格
        while twice is not None and twice.next is not None:
            once = once.next
            twice = twice.next.next
        once.next = once.next.next
        return head