"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def dfs(head):
            if not head:
                return
            node,last = head, head
            while node:
                if not node.next:
                    last = node
                if node.child:
                    old_next = node.next
                    node.next = node.child
                    node.child.prev = node
                    tmp_tail = dfs(node.child)
                    node.child = None
                    if old_next:
                        tmp_tail.next = old_next
                    if old_next:
                        old_next.prev = tmp_tail
                    node = old_next
                else:
                    node = node.next

            return last # tail


        if not head:
            return head
        dfs(head)
        return head

