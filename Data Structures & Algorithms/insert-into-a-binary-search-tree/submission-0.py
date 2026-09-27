# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def BSTsearch(node: TreeNode, val: int):
            if node.val > val:
                if node.left is None:
                    node.left = TreeNode(val)
                    return
                BSTsearch(node.left, val)
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                    return
                BSTsearch(node.right, val)
        BSTsearch(root, val)
        return root