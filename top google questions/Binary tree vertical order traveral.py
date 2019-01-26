# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        pre-order traversal;
        dfs;
        hash table
        """
        def dfs(node, depth, degree):
            if node:
                dg_list[degree].append((depth, node))
                dfs(node.left, depth+1, degree - 1)
                dfs(node.right, depth+1, degree + 1)

        if not root:
            return []

        dg_list = defaultdict(list)



        dfs(root, 0, 0)
        return [[tt[1].val for tt in sorted(dg_list[xx], key = lambda x: x[0])] for xx in sorted(dg_list)]




    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        pre-order traversal;
        bfs;
        hash table
        """
        if not root:
            return []

        dg_list = defaultdict(list)
        queue = [(root, 0)]
        while queue:
            cnode, cdg = queue.pop(0)
            dg_list[cdg].append(cnode.val)
            if cnode.left:
                queue.append((cnode.left, cdg - 1))
            if cnode.right:
                queue.append((cnode.right, cdg + 1))


        return [ dg_list[xx] for xx in sorted(dg_list)]