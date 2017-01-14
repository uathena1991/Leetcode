"""
Note:
	1) The node fast and slow meets is not the beginning of the cycle -- it can be anywhere within the loop
	2) distance (head to meet) = distance(meet to start) See:
 https://siddontang.gitbooks.io/leetcode-solution/content/linked_list/linked_list_cycle.html
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        isCycle = False
        if not head or not head.next:
            return None
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                isCycle = True
                break
        if not isCycle:
            return None
        else:
            while slow != head:
                head = head.next
                slow = slow.next
            return slow