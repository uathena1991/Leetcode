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
        n1 = l1
        n2 = l2
        carry = 0
        last1 = l1
        last2 = l2
        while n1 and n2:
            tmp = n1.val+n2.val+carry
            n1.val = tmp%10
            carry = tmp/10
            last1 = n1
            last2 = n2
            n1 = n1.next
            n2 = n2.next
        if n1:
            while n1:
                tmp = n1.val+carry
                n1.val = tmp%10
                carry = tmp/10
                last1 = n1
                n1 = n1.next
        elif n2:
            last1.next = n2
            while n2:
                tmp = n2.val+carry
                n2.val = tmp%10
                carry = tmp/10
                last1 = n2
                n2 = n2.next
        if carry == 1:
            last1.next = ListNode(1)
        # other digit

        return l1



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
        carry = 0
        n1, n2 = l1, l2
        while n1 and n2:
            if not n1.next and n2.next:
                n1.next = ListNode(0)
                n1.next.next = None
            if not n2.next and n1.next:
                n2.next = ListNode(0)
                n2.next.next = None
            n1.val, carry = (n1.val + n2.val + carry)%10, int((n1.val + n2.val + carry)/10)
            if not(n1.next) and not(n2.next) and carry == 1:
                n1.next = ListNode(1)
                n1.next.next = None
            n1, n2 = n1.next, n2.next
        return l1

