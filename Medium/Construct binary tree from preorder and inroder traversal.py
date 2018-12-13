# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def recursive(preorder, inorder):
            if not inorder:
                return None
            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            index = inorder.index(root_val)
            root.left = recursive(preorder, inorder[:index])
            root.right = recursive(preorder, inorder[index+1:])
            return root

        return recursive(preorder, inorder)
