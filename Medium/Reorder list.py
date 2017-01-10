# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def print_node(self):
		print self.val
		if self.next:
			print self.next.val,'\n '
		else:
			print '\n'

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        curr_node = head
        lists = []
        while curr_node:
            lists.append(curr_node)
            curr_node = curr_node.next
        curr_node = head
        idx1 = 0
        idx2 = len(lists)-1
        while idx1<idx2:
            lists[idx1].next = lists[idx2]
            idx1+=1
            lists[idx2].next = lists[idx1]
            idx2-=1
        lists[idx1].next = None

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
lists = [n1,n2,n3]
a = Solution()
a.reorderList(n1)
n1.print_node()
n2.print_node()
n3.print_node()
n4.print_node()