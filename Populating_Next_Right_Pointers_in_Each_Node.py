# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
#
# class Solution:
#     # @param root, a tree link node
#     # @return nothing
#     def connect(self, root):
#         if not root: # []
#             return root
#         curr_root = [root]
#         while curr_root[0].left:
#             tmp = []
#             next_roots =[]
#             for root in curr_root:
#                 # link root.left to root.right
#                 root.left.next = root.right
#                 # link right to next parent's left
#                 if tmp:
#                     tmp.next = root.left
#                 # update tmp
#                 tmp = root.right
#                 next_roots.append(root.left)
#                 next_roots.append(root.right)
#             curr_root = next_roots



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
        curr_roots = [root]
        while curr_roots[0].left or curr_roots[0].right:
            next_roots =[]
            for ind in range(len(curr_roots)):
                rt = curr_roots[ind]
                if ind<=len(curr_roots)-2:
                    next_rt = curr_roots[ind+1]
                else:
                    next_rt = []
                # link root.left to root.right
                if rt.left:
                    if rt.right:
                        rt.left.next = rt.right
                    elif next_rt and next_rt.left:
                        rt.left.next = next_rt.left
                    elif next_rt and next_rt.right:
                        rt.left.next = next_rt.right
                    next_roots.append(rt.left)
                # link right to next parent's left
                if rt.right:
                    if next_rt and next_rt.left:
                        rt.right.next = next_rt.left
                    elif next_rt and next_rt.right:
                        rt.right.next = next_rt.right
                    next_roots.append(rt.right)
            curr_roots = next_roots



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
        if not root or (not root.left and not root.right):
            return
        if root.left and root.right:
            root.left.next = root.right
        next_node = self.find_next(root.next)
        if root.right:
            root.right.next = next_node
        else:
            root.left.next = next_node
        self.connect(root.right)
        self.connect(root.left)

    def find_next(self,root): # find the next root to expand: DFS
        if not root:
            return None
        if not root.left and not root.right:
            return self.find_next(root.next)
        if root.left:
            return root.left
        if root.right:
            return root.right
