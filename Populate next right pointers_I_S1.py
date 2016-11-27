# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: # []
            return root
        curr_root = [root]
        while curr_root[0].left:
            tmp = []
            next_roots =[]
            for root in curr_root:
                # link root.left to root.right
                root.left.next = root.right
                # link right to next parent's left
                if tmp:
                    tmp.next = root.left
                # update tmp
                tmp = root.right
                next_roots.append(root.left)
                next_roots.append(root.right)
            curr_root = next_roots



