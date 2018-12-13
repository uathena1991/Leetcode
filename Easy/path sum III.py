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
        :rtype: int
        """
        # brute force method
#         def helper(node, sum):
#             if not node:
#                 return 0
#             return int(sum == node.val) + helper(node.left, sum - node.val) + helper(node.right, sum-node.val)
        
#         def traverse_tree(node):
#             if not node:
#                 return 0
#             return helper(node, sum) + traverse_tree(node.left) + traverse_tree(node.right)
        
#         return traverse_tree(root)
        
        # memorization method with dictionary
        def dfs(node, curr_sum):
            if not node:
                return
            curr_sum += node.val
            old_sum = curr_sum - sum
            self.res += cache[old_sum]
            cache[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            cache[curr_sum] -= 1
        from collections import defaultdict
        cache = defaultdict(int)
        cache[0] = 1
        self.res = 0

            
        

        dfs(root, 0)
        return self.res