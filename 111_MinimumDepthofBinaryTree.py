# 111 Minimum Depth of Binary Tree
# 二分木の深さのうち最も浅いもの

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.right == None:
            return 1 + self.minDepth(root.left)
        if root.left == None:
            return 1 + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left),self.minDepth(root.right))