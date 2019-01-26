# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq as hq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def recursive():
            if not self.heap:
                return None
            min_head = hq.heappop(self.heap)[1]
            if min_head.next:
                hq.heappush(self.heap, (min_head.next.val, min_head.next))
            min_head.next = recursive()
            return min_head
        if not lists:
            return []
        if len(lists) == 1:
            return lists[0]

        self.heap = []
        for ll in lists:
            if ll:
                hq.heappush(self.heap, (ll.val, ll))
        if not self.heap:
            return []
        head = hq.heappop(self.heap)[1]
        if head.next:
            hq.heappush(self.heap, (head.next.val, head.next))
        head.next = recursive()
        return head


