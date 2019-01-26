"""
BFS: memorize position in each level of depth
"""
class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        BFS
        """
        if not root:
            return 0
        queue = [(root, 0, 0)] # node, depth, position in curr depth
        curr_depth, max_width, left_p = 0, 0, 0
        while queue:
            cnode, cdepth, cpos = queue.pop(0)
            if cnode:
                queue.append((cnode.left, cdepth + 1, cpos*2))
                queue.append((cnode.right, cdepth + 1, cpos*2 + 1))
                if curr_depth != cdepth:
                    curr_depth, left_p = cdepth, cpos
                max_width = max(cpos - left_p + 1, max_width)
        return max_width


"""
BFS: create None node
"""

class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        BFS
        """
        if not root:
            return 0
        next_level = [root]
        max_width = 1
        while any(next_level):
            curr_level, next_level = next_level, []
            for idx, cc in enumerate(curr_level):
                if not cc:
                    if idx < len(curr_level) - 1:
                        next_level.append(None)
                        next_level.append(None)
                elif cc.right or cc.left: # has right child or right child
                    [next_level.append(cc.left) if cc.left else next_level.append(None)] # add left node, or None
                    [next_level.append(cc.right) if cc.right else next_level.append(None)] # add left node, or None
                elif idx < len(curr_level) - 1: # has no children, but not the rightmost node
                    next_level.append(None)
                    next_level.append(None)
            while next_level and not next_level[-1]:
                next_level.pop()
            while next_level and not next_level[0]:
                next_level.pop(0)

            # tmp_nl = []
            # for nn in next_level:
                # tmp_nl.append(nn.val) if nn else tmp_nl.append(nn)
            # print(tmp_nl)
            max_width = max(max_width, len(next_level))

        return max_width


"""
DFS: memorize depth and position for each node
"""

class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        DFS
        """
        def dfs(node, depth, pos):
            if node:
                left_p.setdefault(depth, pos)
                self.max_width = max(self.max_width, pos - left_p[depth] + 1)
                dfs(node.left, depth+1, pos*2)
                dfs(node.right, depth+1, pos*2 + 1)


        if not root:
            return 0
        self.max_width = 1
        left_p = dict()
        dfs(root, 0, 0)
        return self.max_width

