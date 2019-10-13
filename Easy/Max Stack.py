class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x,x))
        else:
            max_ele = max(self.stack[-1][1],x)
            self.stack.append((x,max_ele))


    def pop(self) -> int:
        return self.stack.pop()[0]


    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        if self.stack[-1][0]==self.stack[-1][1]:
            return self.stack.pop()[0]
        else:
            maxi = self.stack[-1][1]
            buffer = []
            while self.stack[-1][0] != maxi:
                buffer.append(self.stack.pop()[0])
            self.stack.pop()
            while buffer:
                self.push(buffer.pop())
            return maxi


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()