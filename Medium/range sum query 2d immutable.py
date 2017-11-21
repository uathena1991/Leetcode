class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.sum_inte = self.cal_sum()

    def cal_sum(self):
        ## calculate sum[i][j], from [0,0] to [i,j]
        if not self.matrix:
            return []
        row_max = len(self.matrix)
        col_max = len(self.matrix[0])
        sum_inte = [[0 for x in range(col_max)] for y in range(row_max)]
        for i in range(row_max):
            sum_row = 0
            for j in range(col_max):
                if i == 0:
                    sum_row += self.matrix[i][j]
                    sum_inte[i][j] = sum_row
                else:
                    sum_row += self.matrix[i][j]
                    sum_inte[i][j] = sum_inte[i-1][j] + sum_row
        return sum_inte



    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        row_max = len(self.matrix)
        col_max = len(self.matrix[0])
        if not (0 <= row1 < row_max and 0 <= row2 < row_max and 0 <= col1 < col_max and 0 <= col2 < col_max):
            return False
        else:
            if row1 == 0 and col1 == 0:
                return self.sum_inte[row2][col2]
            elif row1 == 0:
                return self.sum_inte[row2][col2] - self.sum_inte[row2][col1-1]
            elif col1 == 0:
                return self.sum_inte[row2][col2] - self.sum_inte[row1-1][col2]
            else:
                return self.sum_inte[row2][col2] - self.sum_inte[row1-1][col2] - self.sum_inte[row2][col1-1] + self.sum_inte[row1-1][col1-1]




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)