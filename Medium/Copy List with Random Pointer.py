# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        curr = head
        # create a copy for each node
        while curr:
            copy_node = RandomListNode(curr.label)
            copy_node.next = curr.next
            curr.next = copy_node
            curr = copy_node.next
        # assign random pointers
        curr = head
        while curr:
            copy_node = curr.next
            curr_random = curr.random
            if curr_random:
                copy_node.random = curr_random.next
            curr = copy_node.next
        # delete old list and have only new list
        curr = head
        newhead = head.next
        while curr:
            tmp = curr.next
            curr.next = tmp.next
            if tmp.next:
                tmp.next = tmp.next.next
            curr = curr.next
        return newhead

a = Solution()
n1 = RandomListNode(-1)
res = a.copyRandomList(n1)
print res.label