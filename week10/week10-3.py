# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# week10-3.py 學習計畫 Binary Tree - DFS 第 3 題
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def visited(node, max_num):
            if node:
                if node.val >= max_num:
                    max_num = node.val
                    self.count += 1
                visited(node.left, max_num)
                visited(node.right, max_num)
        visited(root, -float('inf'))
        return self.count
        