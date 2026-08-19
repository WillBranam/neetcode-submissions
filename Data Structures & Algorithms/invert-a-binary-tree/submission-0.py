# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def swap(root):
            if not root:
                return None
            leftNode = root.left
            rightNode = root.right
            temp = leftNode
            root.left = rightNode
            root.right = temp
            swap(leftNode)
            swap(rightNode)
        swap(root)
        return root
