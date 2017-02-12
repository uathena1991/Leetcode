class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dull_head = ListNode(-1)
        dull_head.next = head
        pre = dull_head
        curr = head
        idx = 0
        while idx <= n-1 and curr:
            if idx == m - 1: # record the last node before [m,n]
                start_prenode = pre
                start_node = curr
                pre = curr
                curr = curr.next
            elif idx > m - 1: #  reverse
                tmp = curr.next
                curr.next = pre
                pre = curr
                curr = tmp
            else:
                pre = curr
                curr = curr.next
            idx += 1
        start_prenode.next = pre
        start_node.next = curr
        return dull_head.next
