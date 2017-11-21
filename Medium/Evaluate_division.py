class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        import collections
        # create a graph to save all edges and weights
        graph = collections.defaultdict(dict)
        for eq,v in zip(equations, values):
            graph[eq[0]][eq[1]] = v
            graph[eq[1]][eq[0]] = 1.0/v
            graph[eq[0]][eq[0]] = graph[eq[1]][eq[1]] = 1.0

        # Floyd algorithm
        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    graph[i][j] = graph[i][k] * graph[k][j]

        return [graph[num].get(den, -1.0) for num, den in queries]
