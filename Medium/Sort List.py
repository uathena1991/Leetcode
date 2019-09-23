# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def find_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        dummy = ListNode(-float('inf'))
        p = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 or l2
        return dummy.next

    def sortList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head
        mid = self.find_mid(head)
        h2 = mid.next
        mid.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(h2)
        return self.merge(l1, l2)
