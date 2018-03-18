# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


## not constant space
class Solution(object):
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        curr_level = [root]
        next_level = []
        while curr_level:
            for idx in range(len(curr_level)):
                if curr_level[idx].left:
                    next_level.append(curr_level[idx].left)
                    next_level.append(curr_level[idx].right)
                if idx < len(curr_level) - 1:
                    curr_level[idx].next = curr_level[idx+1]
            curr_level = next_level
            next_level = []



## constant space (with two pointers)

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        pre_level = root
        curr_level = None
        while pre_level.left:
            curr_level = pre_level
            while curr_level:
                curr_level.left.next = curr_level.right
                if curr_level.next:
                    curr_level.right.next = curr_level.next.left
                curr_level = curr_level.next
            pre_level = pre_level.left






