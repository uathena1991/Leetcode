from collections import defaultdict
class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for p, pp in zip(pid, ppid):
            graph[pp] += [p]

        # print(graph)
        queue = [kill]
        res = []
        while queue:
            curr = queue.pop(0)
            res.append(curr)
            for kid in graph[curr]:
                queue.append(kid)

        return res
                