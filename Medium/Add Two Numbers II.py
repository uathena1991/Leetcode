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



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def node_2_list(l1):
            res = []
            while l1:
                res.append(l1.val)
                l1 = l1.next
            return res
        list1 = node_2_list(l1)
        list2 = node_2_list(l2)
        len_list1 = len(list1)
        len_list2 = len(list2)
        list1 = [0]*max(0, len_list2 - len_list1) + list1
        list2 = [0]*max(0, len_list1 - len_list2) + list2
        res = []
        carry = 0
        while len(list1) > 0:
            t1 = list1.pop()
            t2 = list2.pop()
            res.append((t1+t2+carry)%10)
            carry = int((t1+t2+carry)/10)
        if carry == 1:
            res.append(1)
        # conver to linked list:
        head = ListNode(res[-1])
        curr = head
        for s in res[-2::`-1]:
            curr.next = ListNode(s)
            curr = curr.next
        curr.next = None
        return head






