# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def recursive(clist):
            mid = len(clist)//2
            if len(clist) < 1:
                return None
            cnode = TreeNode(clist[mid])
            cnode.left = recursive(clist[0:mid])
            cnode.right = recursive(clist[mid + 1:])
            return cnode

        # find middle points of the linked list
        slist = []
        while head:
            slist.append(head.val)
            head = head.next
        # print(slist)
        ## define root
        # root = TreeNode(slist[len(slist)//2])

        # root.left = recursive(slist[:len(slist)//2])
        # root.right = recursiveslist[len(slist)//2+1:])
        return recursive(slist)

            