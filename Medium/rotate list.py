# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head
        old_last = head
        len = 1
        while old_last.next:
            old_last = old_last.next
            len+=1
        old_last.next = head
        # find start/end
        new_last = head
        t = len-k%len
        while t > 1:
            new_last = new_last.next
            t-=1
        new_start = new_last.next
        new_last.next = None
        return new_start
            

