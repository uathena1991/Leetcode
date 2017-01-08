# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def generate_LRTrees(self,min_root,max_root):
        if min_root > max_root:
            return [None]
        # if min_root == max_root:
        #     return [TreeNode(min_root)]
        res = []
        for root in range(min_root,max_root+1):
            left_trees = self.generate_LRTrees(min_root,root-1)
            right_trees = self.generate_LRTrees(root+1,max_root)
            for l in left_trees:
                for r in right_trees:
                    root_node = TreeNode(root)
                    root_node.left = l
                    root_node.right = r
                    res.append(root_node)
        return res
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        return self.generate_LRTrees(1,n)



