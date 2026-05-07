# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# week11-4.py 學習計畫 Binary Search Tree 第 2 題
# Leetcode 450. Delete Node in a BST
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def DelNode(root, key):
            if root is None:
                return None
            if key > root.val:
                root.right = DelNode(root.right, key)
            elif key < root.val:
                root.left = DelNode(root.left, key)
            else:
                if root.right is None:
                    return root.left
                if root.left is None:
                    return root.right
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.val = temp.val
                root.right = DelNode(root.right, temp.val)
            return root
        return DelNode(root, key)