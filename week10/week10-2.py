# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# week10-2a.py 學習計畫 Binary Tree - DFS 第 1 題
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def travel(root, count):
            if root:
                left = travel(root.left, count + 1)
                right = travel(root.right, count + 1)
            else:
                return count - 1
            return max(left, right)
        return travel(root, 1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# week10-2b.py 學習計畫 Binary Tree - DFS 第 1 題
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
