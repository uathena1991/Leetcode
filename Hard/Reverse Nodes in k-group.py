# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def check_k_steps_ahead(k, curr):
            for i in range(k - 1):
                if not curr:
                    return None
                curr = curr.next
            return curr

        def helper(curr, pre_last, curr_last, next_head):
            """reverse and return """
            new_last = curr
            pre_last.next = curr_last
            pre, curr= curr, curr.next
            while curr != next_head:
                tmp = curr.next
                curr.next = pre
                pre = curr
                curr = tmp
            new_last.next = curr
            return curr, new_last

        # def print_linked_list(head):
        #     res = []
        #     while head:
        #         res.append(head.val)
        #         head = head.next
        #     return res

        if k == 1:
            return head

        pre_last = ListNode(0)
        curr = head
        new_head = check_k_steps_ahead(k, curr)
        if not new_head:
            return head
        curr_last = new_head

        while curr and curr_last:
            curr_last = check_k_steps_ahead(k, curr)
            if curr_last:
                print("LAST, curr:", curr_last.val, curr.val)
                curr, pre_last = helper(curr, pre_last, curr_last, curr_last.next)
                # print(curr.val)
                # print(print_linked_list(new_head))

        return new_head


