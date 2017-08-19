class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.list) == 0:
            tmp_min = x
        else:
            tmp_min = min(x, self.list[-1][1])
        self.list.append([x, tmp_min])


    def pop(self):
        """
        :rtype: void
        """
        if len(self.list) == 0:
            return None
        else:
            self.list.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.list[-1][0]


    def getMin(self):
        """
        :rtype: int
        """
        return self.list[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()