"""
Inverse the first half (or to be concise-- when you reach 3-4-3, or 3-3),
and compare the first half with the second half.
test case:
[1,2,2,1]
[1,1]
[1,2,3,3,2,1]
[1,2,3,2,1]
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # when len(list)<=2
        if not head or not head.next:
            return True
        if not head.next.next:
            if head.next.val == head.val:
                return True
            else:
                return False
        # normal case
        nnext = head.next
        curr = head
        prev = None
        while not prev or not (prev.val == nnext.val or prev.val ==curr.val): # reverse first half
            curr.next = prev # reverse the list
            prev = curr
            curr = nnext
            nnext = nnext.next
            if not (prev and nnext and curr):
                return False
        # compare first half(curr) with second half(nnext)
        if prev.val == nnext.val:
            head1 = prev
            head2 = nnext
        elif prev.val == curr.val:
            head1 = prev
            head2 = curr
        while head1 and head2:
            if head1.val != head2.val:
                return False
            else:
                head1 = head1.next
                head2 = head2.next
        if head1 or head2:
            return False
        else:
            return True

def create_list(list):
	head = ListNode(list.pop())
	while list:
		head.next = ListNode(list.pop())
		head = head.next
	return head


# a1 = ListNode(1)
# a2 = ListNode(2)
# a1.next = a2
# a3 = ListNode(3)
# a2.next = a3
# a4 = ListNode(4)
# a3.next = a4
# a5 = ListNode(3)
# a4.next = a5
# a6 = ListNode(2)
# a5.next = a6
# a7 = ListNode(1)
# a6.next = a7
lists = create_list([1,2,2,3])
a = Solution()
print a.isPalindrome(lists)