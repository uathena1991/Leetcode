# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(node, parent):
            if not node:
                return
            node.par = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)
        queue = [(target, 0)]
        res = []
        visited = []
        # bfs search
        while len(queue) > 0:
            curr = queue[0]
            visited.append(curr[0])
            if curr[1] == K:
                return [x[0].val for x in queue]
            queue.pop(0)
            for nei in [curr[0].par, curr[0].left, curr[0].right]:
                if nei and nei not in visited:
                    queue.append((nei, curr[1] + 1))
        return []

