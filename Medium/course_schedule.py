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

