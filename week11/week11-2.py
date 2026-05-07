# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# week11-1.py 學習計畫 Binary Tree - DFS 第1題
# Leetcode 236. Lowest Common Ancestor of a Binary Tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = []
        self.count = 0
        def travel(root, target1, target2):
            if root:
                l_target1, l_target2 = travel(root.left, target1, target2)
                r_target1, r_target2 = travel(root.right, target1, target2)
                if (root == p or l_target1 or r_target1) and (root == q or l_target2 or r_target2):
                    self.ans.append(root)
                if root == p:
                    return True, l_target2 or r_target2
                if root == q:
                    return l_target1 or r_target1, True
                return l_target1 or r_target1, l_target2 or r_target2
            else:
                return False, False
        travel(root, False, False)
        return self.ans[0]
