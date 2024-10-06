# 108 Convert Sorted Array to Binary Search Tree
# ソートされた配列をいい感じの二分木にする


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums) // 2
        bst = TreeNode(nums[mid])
        bst.left = self.sortedArrayToBST(nums[:mid])
        bst.right = self.sortedArrayToBST(nums[mid+1:])
        return bst

