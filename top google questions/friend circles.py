"""
bfs
"""
class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # bfs
        def bfs(i):
            queue.append(i)
            while len(queue) > 0:
                cr = queue.pop(0)
                visited[cr] = 1
                for cc in range(len(M)):
                    if M[cr][cc] == 1 and visited[cc] == 0:
                        queue.append(cc)
            return

        visited = [0]*len(M[0])
        res = 0
        queue = []
        for i in range(len(M)):
            if visited[i] == 0:
                bfs(i)
                res += 1
        return res



"""
dfs
"""
class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # dfs
        def dfs(stack, i):
            while len(stack) > 0:
                curr = stack.pop()
                set_all.remove(curr)
                for i in range(len(M)):
                    if i in set_all and M[curr][i] == 1:
                        stack.append(i)
                        dfs(stack, i)
            return

        set_all = set([x for x in range(len(M))])
        res  = 0
        for i in range(len(M)):
            stack = []
            if i in set_all:
                stack.append(i)
                dfs(stack, i)
                res += 1
        return res

