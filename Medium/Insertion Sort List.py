# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fake_head = ListNode(-float('Inf'))
        curr = head
        while curr:
            nnext = curr.next
            prev = fake_head
            # find insert location
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            # insert
            curr.next = prev.next
            prev.next = curr
            curr = nnext

        return fake_head.next

a = Solution()
head = ListNode(3)
head.next = ListNode(9)
head.next.next = ListNode(1)
new =  a.insertionSortList(head)
print new.val,new.next.val,new.next.next.val

