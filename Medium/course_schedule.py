class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for x in range(numCourses)]
        visited = [0 for x in range(numCourses)]
        for x,y in prerequisites:
            graph[x].append(y)

        def dfs(n):
            if visited[n] == -1:
                return False
            if visited[n] == 1:
                return True
            visited[n] = -1
            for j in graph[n]:
                if not dfs(j):
                    return False
            visited[n] = 1
            return True

        for x in range(numCourses):
            if not dfs(x):
                return False
        return True



"""
Topological sorting
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        graphs = defaultdict(list)
        in_degree = defaultdict(int)
        for pr in prerequisites:
            graphs[pr[0]].append(pr[1])
            in_degree[pr[1]] += 1
        queue = [x for x in range(numCourses) if in_degree[x]==0]
        curr = []
        while queue:
            curr.append(queue.pop(0))
            for child in graphs[curr[-1]]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)
        print(curr)
        return len(curr) == numCourses



