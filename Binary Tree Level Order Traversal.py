# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
        print_list =[]
        if not root:
            return print_list
        curr_root = [root]
        while curr_root:
            next_root = []
            print_list.append([nroot.val for nroot in curr_root])
            for nroot in curr_root:
                if nroot.left:
                    next_root.append(nroot.left)
                if nroot.right:
                    next_root.append(nroot.right)
            curr_root = next_root
        return print_list
