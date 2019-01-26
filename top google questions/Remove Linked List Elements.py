# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        sudohead = ListNode(float('inf'))
        sudohead.next = head
        pre, curr = sudohead, head
        while curr:
            if curr.val != val:
                pre = curr
                curr = curr.next
            else:
                curr = curr.next
                pre.next = curr
                # pre = curr
                # curr = curr.next

        return sudohead.next
                