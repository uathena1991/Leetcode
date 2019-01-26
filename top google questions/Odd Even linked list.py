# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        ohead, ehead = head, head.next
        ocurr, ecurr = head, head.next
        opre, epre = ListNode(-1), ListNode(-1)
        opre.next = epre
        epre.next = ocurr
        while ocurr and ecurr:
            opre.next = ocurr
            epre.next = ecurr
            opre, epre = ocurr, ecurr
            ocurr = ocurr.next.next
            ecurr = ecurr.next.next if ocurr else None
        if not ocurr:
            opre.next = ehead
        else:
            opre.next = ocurr
            ocurr.next = ehead
            epre.next = ecurr

        return head