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
        start_node.next = tmp

        return dull_head.next

# second solution
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
        dump_head = ListNode(0)
        dump_head.next = head
        idx = 1
        pre = dump_head
        curr = head
        while idx <= n and curr: #???
            if idx == m: # record old start node
                ostart = pre
                ofirst = curr
            if idx > m: # reverse
                nnext = curr.next
                curr.next = pre
                pre = curr
                curr = nnext
            else:
                pre = curr
                curr = curr.next
            idx += 1
        # print ostart.val, ofirst.val, pre.val, curr.val
        ostart.next = pre
        ofirst.next = curr

        return dump_head.next


a = Solution()
head = leetlib.ListNode(3).create_listnode([1,2,3,4,5])
leetlib.ListNode(3).printout_listnode(head)
leetlib.ListNode(3).printout_listnode(a.reverseBetween(head,3,4))