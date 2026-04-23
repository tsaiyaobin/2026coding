# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# week09-2.py 學習計畫 Linked List 第 3 題
# Leetcode 206. Reverse Linked List
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while head is not None:
            temp.append(head.val)
            head = head.next
        
        N = len(temp)
        dummy = ListNode()
        cur = dummy
        for i in range(N):
            Node = ListNode(temp[N-i-1])
            dummy.next = Node
            dummy = dummy.next
        return cur.next
