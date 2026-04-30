# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# week10-5.py 學習計畫 Binary Tree - DFS 第 4 題
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = Counter()
        counter[0] = 1
        self.ans = 0
        def travel(root, total):
            if root:
                total += root.val
                self.ans += counter[total - targetSum]
                counter[total] += 1
                travel(root.left, total)
                travel(root.right, total)
                counter[total] -= 1
        travel(root, 0)
        return self.ans