"""
805. Split Array With Same Average

In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)

Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.

Example :
Input:
[1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
Note:

The length of A will be in the range [1, 30].
A[i] will be in the range of [0, 10000].
"""

## failed submission
## sort first, then for each element, try to decide which sublist to go
## failed case: [2,0,5,6,16,12,15,12,4] true, return False
class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 2:
            return False
        if len(A) == 2:
            return False if A[0] != A[1] else True

        mean_A = float(sum(A))/len(A)
        A = sorted(A, reverse=True)
        print A
        B = [A[0]]
        C = [A[1]]
        for idx in range(len(A)-1, 1, -1):
            mean_B = float(sum(B))/len(B)
            mean_C = float(sum(C))/len(C)
            if mean_B < mean_C: # make B larger or C smaller
                if A[idx] >= len(B):
                    B.append(A[idx])
                else:
                    C.append(A[idx])
            else:
                if A[idx] >= len(C):
                    C.append(A[idx])
                else:
                    B.append(A[idx])
        print B
        print C
        return float(sum(B))/len(B) == float(sum(C))/len(C)



#### still failed... why...
## failed case: [2,0,5,6,16,12,15,12,4] true, return False
class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 2:
            return False
        if len(A) == 2:
            return False if A[0] != A[1] else True

        mean_A = float(sum(A))/len(A)
        A = sorted(A, reverse = True)
        print A
        B = [A[0]]
        C = [A[1]]
        for idx in range(len(A)-1, 1, -1):
            mean_B = float(sum(B))/len(B)
            mean_C = float(sum(C))/len(C)
            # decide which sublist to go
            new_mb = float((mean_B * len(B) + A[idx])) / (len(B) + 1)
            new_mc = float((mean_C * len(C) + A[idx])) / (len(C) + 1)
            if abs(new_mb - mean_A) < abs(new_mc - mean_A):
                B.append(A[idx])
            else:
                C.append(A[idx])
        print B
        print C
        return float(sum(B))/len(B) == float(sum(C))/len(C)





