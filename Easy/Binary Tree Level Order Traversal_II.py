# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
        results =[]
        if not root:
            return []
        results.append([root.val]);
        curr_roots = [root];
        while curr_roots:
            curr_kids = []
            tmp_roots = []
            for r in curr_roots:
                if r.left:
                    curr_kids.append(r.left.val)
                    tmp_roots.append(r.left)
                if r.right:
                    curr_kids.append(r.right.val)
                    tmp_roots.append(r.right)
            if curr_kids:
                results.append(curr_kids)
            curr_roots = tmp_roots
        results.reverse()
        return results
