import heapq as hq
class MyCalendarTwo:

    def __init__(self):
        self.heap  = [] # heap
        self.dbbook = [] # record periods that have two books

    def book(self, start: int, end: int) -> bool:
        if not self.heap:
            hq.heappush(self.heap, [start, end])
            return True
        # check
        for s,e in self.dbbook:
            if end <= s or start >= e:
                continue
            else:
                return False
        # update double book list
        for s,e in self.heap:
            if start >= e or end <= s:
                continue
            # print(s,e)
            hq.heappush(self.dbbook, [max(start,s), min(e,end)])
        # insert
        hq.heappush(self.heap, [start, end])
        return True




# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)