# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.dict = {} # val: node
        def in_order_traversal(node):
            if not node:
                return
            if node.left:
                in_order_traversal(node.left)
            self.dict[node.val] = node
            if node.right:
                in_order_traversal(node.right)

        in_order_traversal(root)
        values = list(self.dict.keys())
        cand, toswitch = None, None
        for i in range(len(values)-1):
            if values[i] >= values[i+1]:
                cand = values[i+1]
        for i in range(len(values)):
            if values[i] > cand:
                toswitch = values[i]
                break
        # print(cand, toswitch)
        # swap

        self.dict[toswitch].val = cand
        self.dict[cand].val = toswitch





