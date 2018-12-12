class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
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


        if len(curr) < numCourses:
            return []
        for i in range(numCourses):
            if i not in curr:
                curr.append(i)

        return curr[::-1]

