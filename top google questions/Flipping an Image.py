class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        inverted = [x[::-1] for x in A]
        return [[int(x == 0) for x in Y] for Y in inverted]