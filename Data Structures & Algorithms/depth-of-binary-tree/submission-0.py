# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(root, d):
            if not root:
                return d
            leftNode = root.left
            rightNode = root.right
            leftDepth = dfs(leftNode, d + 1)
            rightDepth = dfs(rightNode, d + 1)
            currMax = max(leftDepth, rightDepth)

            return currMax
        return dfs(root,0)
        