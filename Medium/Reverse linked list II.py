# # Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
import leetcode_tool_lib as leetlib
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
        for idx in range(m-1):
            pre = pre.next
        start_prenode = pre
        start_node = pre.next
        curr = pre.next
        for idx in range(m,n):
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        tmp = curr.next
        curr.next = pre
        print curr.val,pre.val,curr.next.val
        print start_prenode.val,start_node.val,curr.val
        start_prenode.next = curr
        start_node.next = curr.next

        # while idx <= n-1 and curr:
        #     if idx == m - 1: # record the last node before [m,n]
        #         start_prenode = pre
        #         start_node = curr
        #         pre = curr
        #         curr = curr.next
        #     elif idx > m - 1: #  reverse
        #         tmp = curr.next
        #         curr.next = pre
        #         pre = curr
        #         curr = tmp
        #     else:
        #         pre = curr
        #         curr = curr.next
        #     idx += 1
        # start_prenode.next = pre
        # start_node.next = curr
        return dull_head.next




a = Solution()
head = leetlib.create_listnode([1,2,3,4,5])
leetlib.printout_listnode(head)
leetlib.printout_listnode(a.reverseBetween(head,1,5))