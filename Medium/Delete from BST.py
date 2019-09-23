# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                # add root.right to the most right node of root.left, and return root.left
                node = root.left
                while node.right:
                    node = node.right
                node.right = root.right
                root.right = None
                return root.left
        return root



