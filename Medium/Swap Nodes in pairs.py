# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur1, cur2 = head, head.next
        pre_tail = ListNode(-1)
        pre_tail.next = head
        new_head = head.next
        while cur1 and cur2:
            cur1.next = cur2.next
            cur2.next = cur1
            pre_tail.next = cur2
            pre_tail = cur1
            cur1= cur1.next
            cur2 = cur1.next if cur1 else None
        return new_head




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        curr1 = head
        curr2= head.next
        new_head = curr2
        while curr1 and curr2:
            nnext = curr2.next
            if nnext and nnext.next:
                nextnext = nnext.next
            else:
                nextnext = None
            curr2.next = curr1
            if nextnext:
                curr1.next = nextnext
            else:
                curr1.next = nnext
            curr1 = nnext
            if curr1:
                curr2 = curr1.next
        return new_head