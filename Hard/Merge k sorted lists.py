"""
PriorityQueue
Note:
 	Get used to Linked lists -- only store current nodes inside the queue
 	store {node.val:node} in the queue
 	dict.getvalues() returns a list
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return []
        if not l1:
            return l2
        if not l2:
            return l1
        pre1 = None
        if l1.val <= l2.val:
            p1,p2 = l1,l2
            p1_next = p1.next
        else:
            p1,p2 = l2,l1
            p1_next = p1.next
        while p1 and p2:
            if (p1_next and p1.val <= p2.val< p1_next.val) or ((not p1_next) and p1.val <= p2.val):
                p1.next = p2
                p2_next = p2.next
                p2.next = p1_next
                p1 = p2
                p2 = p2_next
            elif p1.val <= p2.val:
                pre = p1
                p1 = p1.next
                if p1:
                    p1_next = p1.next
            elif p1.val > p2.val:
                p2 = p2.next
        if p2:
            pre.next = p2
        if l1.val <= l2.val:
            return l1
        else:
            return l2

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue
        res = None
        prior_queue = PriorityQueue()
        # put heads inside priority queue
        for head in lists:
            if head:
                prior_queue.put({head.val:head})
        # compare values in all the lists
        while not prior_queue.empty():
            tmp_value = prior_queue.get()
            curr_node = tmp_value.values()[0]
            if not res:
                res = curr_node
            else:
                pre.next = curr_node
            pre = curr_node
            if curr_node.next:
                # put next node in the queue
                prior_queue.put({curr_node.next.val:curr_node.next})
        return res


