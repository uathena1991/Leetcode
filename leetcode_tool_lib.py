"""
Define a few functions that are commonly used in leetcode
"""
# create singly-linked ListCode
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def create_listnode(list):
	if not list:
		return None
	head = ListNode(list[0])
	curr = head
	for i in list[1:]:
		post = ListNode(i)
		curr.next = post
		curr = post
	return head

def printout_listnode(head):
	curr = head
	res = []
	while curr:
		res.append(curr.val)
		curr = curr.next
	print res
	return res
