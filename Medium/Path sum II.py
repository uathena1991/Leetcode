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


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
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
        if not root:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])]
        while stack:
            node, c_sum, c_path = stack.pop()
            if not node.left and not node.right and c_sum == 0:
                res.append(c_path)
            if node.left:
                stack.append((node.left, c_sum-node.left.val, c_path + [node.left.val]))
            if node.right:
                stack.append((node.right, c_sum-node.right.val, c_path + [node.right.val]))

        return res
        
                
        