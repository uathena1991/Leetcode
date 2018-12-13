# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        dummy_head = ListNode(0)
        dummy_head.next = head

        curr, pre_tail = head, dummy_head

        while curr and curr.next:
            pre_tail.next = curr.next
            curr.next = curr.next.next
            pre_tail.next.next = curr
            pre_tail = curr
            curr = curr.next

        return dummy_head.next