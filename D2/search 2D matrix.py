class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def frecursive(low_bd,high_bd,mid,matrix,target):
            if low_bd<mid<high_bd:
                if matrix[low_bd/num_col][low_bd%num_col] <= target < matrix[mid/num_col][mid%num_col]:
                    return frecursive(low_bd,mid,(low_bd+mid)/2,matrix,target)
                elif matrix[mid/num_col][mid%num_col] <= target <= matrix[high_bd/num_col][high_bd%num_col]:
                    return frecursive(mid,high_bd,(mid+high_bd)/2,matrix,target)
                else:
                    return False
            elif target == matrix[low_bd/num_col][low_bd%num_col] or target == matrix[high_bd/num_col][high_bd%num_col] or target == matrix[mid/num_col][mid%num_col]:
                return True
            else:
                return False

        if not matrix:
            return False
        num_row = len(matrix)
        num_col = len(matrix[0])
        low_bd = 0
        high_bd = num_row*num_col-1
        mid = (low_bd + high_bd)/2
        return frecursive(low_bd,high_bd,mid,matrix,target)
