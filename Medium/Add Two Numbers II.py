# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def push_into_stack(l):
            res = []
            cur = l
            while cur:
                res.append(cur.val)
                cur = cur.next
            return res

        stack1 = push_into_stack(l1)
        stack2 = push_into_stack(l2)
        res = []
        carry = 0
        while len(stack1) > 0 or len(stack2) > 0:
            curr1 = stack1.pop() if len(stack1) > 0 else 0
            curr2 = stack2.pop() if len(stack2) > 0 else 0
            tmp = curr1 + curr2 + carry
            carry = 1 if tmp >= 10 else 0
            tmp = tmp - 10 if tmp >= 10 else tmp
            res.append(tmp)
        if carry == 1:
            res.append(1)
        res = res[::-1]
        # print res
        # convert to linked list
        head = ListNode(res[0])
        res_l = head
        for idx in range(1, len(res)):
            res_l.next = ListNode(res[idx])
            res_l = res_l.next

        return head