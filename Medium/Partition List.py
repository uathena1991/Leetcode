"""
create two lists: small, and other, link them together in the end
Note: if x < min(list) or x>max(list)
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        small = ListNode('Inf')
        large = ListNode('Inf')
        curr_node = head
        new_head = head
        large_head = head
        idx_s = 0
        idx_l = 0
        while curr_node:
            if curr_node.val < x:
                if idx_s == 0:
                    new_head = curr_node
                small.next = curr_node
                small = curr_node
                idx_s+=1
            else:
                if idx_l == 0:
                    large_head = curr_node
                large.next = curr_node
                large = curr_node
                idx_l+=1
            curr_node = curr_node.next
        if idx_l>0:
            small.next = large_head
            large.next = None
        return new_head
            
        
