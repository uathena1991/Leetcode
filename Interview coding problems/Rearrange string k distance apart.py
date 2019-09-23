import heapq as hq
from collections import Counter
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        counts_task = Counter(s)
        task_tuple = [(-counts_task[tt], tt) for tt in counts_task]
        hq.heapify(task_tuple)
        res_list = []
        while task_tuple:
            tmp, idx = [], 0
            while idx < k and task_tuple:  # pop top k
                curr_max = hq.heappop(task_tuple)
                res_list.append(curr_max[1])
                if curr_max[0] + 1 < 0:
                    tmp.append((curr_max[0]+1, curr_max[1]))
                idx += 1
            if idx < k and tmp:
                return ""
            # combine tmp and task_tuple
            while tmp:
                hq.heappush(task_tuple, tmp.pop())
            # print(res_list)
        return "".join(res_list)