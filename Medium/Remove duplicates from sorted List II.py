# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        if head.next.val == head.val and not head.next.next:
            return []

        dummy = ListNode(head.val - 1)
        dummy.next = head
        pre, curr, nnext = dummy, head, head.next
        while curr and nnext:
            if curr.val != nnext.val:
                pre = curr
                curr = nnext
                nnext = nnext.next
            else:
                while curr and nnext and curr.val == nnext.val:
                    curr = nnext
                    nnext = nnext.next
                pre.next = nnext
                curr = nnext
                nnext = nnext.next if nnext else None

        return dummy.next

