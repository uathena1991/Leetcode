"""
test cases:
[12,null,-60] [12,null,72]
[1] []
[1,2] [1,2,3]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        tmp_p = [p]
        tmp_q = [q]
        if p == None and q == None:
            return True
        elif p ==None or q == None:
            return False
        while len(tmp_p)>0 and len(tmp_q)>0:
            curr_p = tmp_p.pop()
            curr_q = tmp_q.pop()
            if curr_p.val == curr_q.val:
                if curr_p.left is not None and curr_q.left is not None:
                    tmp_p.append(curr_p.left)
                    tmp_q.append(curr_q.left)
                elif not (curr_p.left is None and curr_q.left is None):
                    return False
                if curr_p.right is not None and curr_q.right is not None:
                    tmp_p.append(curr_p.right)
                    tmp_q.append(curr_q.right)
                elif not (curr_p.right is None and curr_q.right is None):
                    return False
            else:
                return False
        return True
        