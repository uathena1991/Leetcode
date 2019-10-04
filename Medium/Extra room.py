class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.st = []


    def seat(self) -> int:
        if not self.st:
            self.st = [0]
            return 0
        max_dis, res = self.st[0], 0
        for i,s in enumerate(self.st[:-1]):
            dist =  (self.st[i+1] - s)//2
            if dist > max_dis:
                res = s + dist
                max_dis = dist
        if max_dis < self.N - 1 - self.st[-1]:
            res = self.N-1
        self.st.append(res)
        self.st.sort()
        return res


    def leave(self, p: int) -> None:
        self.st.remove(p)



# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)