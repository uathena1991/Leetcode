# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return
        slow, fast = head, head
        i = 0
        while fast and i <= n:
            fast = fast.next
            i += 1
        if i == n and not fast:
            return head.next # delete the first element
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
        