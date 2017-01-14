# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self,  x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def recursion_f(root, sum, curr_path, result):
            if not root:
                return
            if not root.left and not root.right and root.val == sum:
                    result.append(curr_path)
                    return
            if root.left:
                lsum = recursion_f(root.left, sum-root.val, curr_path+[root.left.val], result)
            if root.right:
                rsum = recursion_f(root.right, sum-root.val, curr_path+[root.right.val], result)

        result = []
        if not root:
            return []
        recursion_f(root, sum, [root.val], result)
        return result
        
        
                
        