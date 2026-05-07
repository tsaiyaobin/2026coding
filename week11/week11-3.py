# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# week11-3.py 學習計畫 Binary Search Tree 第一題
# Leetcode 700. Search in a Binary Search Tree
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def travel(root):
            if root:
                if val < root.val:
                    return travel(root.left)
                if val > root.val:
                    return travel(root.right)
                if val == root.val:
                    return root
        return travel(root)