from collections import defaultdict, Counter
"""
Sort
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts_task = Counter(tasks)
        # print(counts_task)
        last_idx = defaultdict(int)
        res = 0
        res_list = []
        while sum(counts_task.values()) > 0:
            sorted_curr = sorted(counts_task, key = lambda x: counts_task[x], reverse = True)
            # print(res, sorted_curr)
            for tt in sorted_curr[:n+1]:
                while last_idx[tt] and -1 <= res - 1 - last_idx[tt] - 1 < n:
                    res_list.append('idle')
                    res += 1
                counts_task[tt] -= 1
                if counts_task[tt] == 0:
                    del counts_task[tt]
                res_list.append(tt)
                last_idx[tt] = res - 1
                res += 1

            # print(res_list, '\n')
        return res





"""
heap
"""
import heapq as hq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts_task = Counter(tasks)
        task_tuple = [(-counts_task[tt], tt) for tt in counts_task]
        hq.heapify(task_tuple)
        res_list = []
        while task_tuple:
            tmp, idx = [], 0
            while idx <= n and task_tuple:  # pop top n
                curr_max = hq.heappop(task_tuple)
                res_list.append(curr_max[1])
                if curr_max[0] + 1 < 0:
                    tmp.append((curr_max[0]+1, curr_max[1]))
                idx += 1
            while idx <= n and tmp:
                res_list.append('idol')
                idx += 1
            # combine tmp and task_tuple
            while tmp:
                hq.heappush(task_tuple, tmp.pop())
        return len(res_list)

