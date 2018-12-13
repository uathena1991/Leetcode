class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def helper(curr, curr_path):
            if curr == len(graph) - 1:
                res.append(curr_path)
            else:
                for node in graph[curr]:
                    helper(node, curr_path + [node])

        res = []
        helper(0, [0])
        return res
