"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def traversal(node):
            if not node:
                return None,None
            # if node.left:
            left_head, left_tail = traversal(node.left)
            if left_tail:
                left_tail.right = node
                node.left = left_tail
            if not left_head:
                left_head = node
            # if node.right:
            right_head, right_tail = traversal(node.right)
            if right_head:
                node.right = right_head
                right_head.left = node
            else:
                right_tail = node
            left_head.left = right_tail
            right_tail.right = left_head
            return left_head, right_tail

        if not root:
            return
        return traversal(root)[0]


