# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def recursive(inorder, postorder):
            if not inorder:
                return None
            root_val = postorder.pop()
            root = TreeNode(root_val)
            index = inorder.index(root_val)
            root.right = recursive(inorder[index+1:], postorder)
            root.left = recursive(inorder[:index], postorder)
            return root


        return recursive(inorder, postorder)