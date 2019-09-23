class RLEIterator:

    def __init__(self, A: List[int]):
        self.queue = [(A[i*2], A[i*2 + 1]) for i in range(len(A)//2) if A[i*2] != 0]
        print(self.queue)


    def next(self, n: int) -> int:
        if not self.queue or self.queue[0][0] == 0:
            return -1
        while self.queue:
            if n < self.queue[0][0]:
                self.queue[0] = (self.queue[0][0] - n, self.queue[0][1])
                return self.queue[0][1]
            c, res = self.queue.pop(0)
            n -= c
            if n == 0:
                return res
        return -1

        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)