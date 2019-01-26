# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]] # put list into stack

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        cnest, cidx = self.stack[-1]
        self.stack[-1][1] += 1
        return cnest[cidx].getInteger()



    def hasNext(self):
        """
        :rtype: bool
        """
        tmp_stack = self.stack
        while tmp_stack:
            cnest, cidx = tmp_stack[-1]
            if cidx == len(cnest):
                tmp_stack.pop()
            else:
                if cnest[cidx].isInteger():
                    # self.stack[-1][1] += 1
                    return True
                else:
                    tmp_stack[-1][1] += 1
                    tmp_stack.append([cnest[cidx].getList(), 0])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())






# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.list.pop().getInteger()


    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.list) == 0:
            return False
        while self.list:
            if self.list[-1].isInteger():
                return True
            else:
                clist = self.list.pop().getList()
                [self.list.append(cc) for cc in clist[::-1]]



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())