class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        from collections import defaultdict
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))


        dist = {node: float('inf') for node in range(1, N+1)}
        dist[K] = 0
        visited = [False] * (N+1)

        while True:
            curr_node = -1
            curr_min = float('inf')
            for x in range(1, N+1):
                if not visited[x] and dist[x] < curr_min:
                    curr_node, curr_min = x, dist[x]

            if curr_node == -1:
                break
            visited[curr_node] = True
            for v, w in graph[curr_node]:
                dist[v] = min(dist[v], dist[curr_node] + w)


        res = max(dist.values())

        return res if res < float('inf') else -1