# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# week11-1.py 學習計畫 Binary Tree - DFS 第2題
# Leetcode 872. Leaf-Similar Trees 
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def travel(root, ans):
            if root:
                if root.left is None and root.right is None: # 找到葉子
                    ans.append(root.val)
                travel(root.left, ans)
                travel(root.right, ans)
            return ans
        return travel(root1, []) == travel(root2, [])

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a = []
        def travel(root):
            if root:
                if root.left is None and root.right is None: # 找到葉子
                    a.append(root.val)
                travel(root.left)
                travel(root.right)
            return a
        travel(root1)
        a, b = [], a
        travel(root2)
        return a == b