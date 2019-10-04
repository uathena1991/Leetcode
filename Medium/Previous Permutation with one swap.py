class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        lenn = len(A)
        i = lenn - 1
        while i > 0 and A[i-1] <= A[i]:
            i -= 1
        if i == 0:
            return A
        left = i - 1
        right = lenn - 1
        while right >= i and A[right] >= A[left]:
            right -= 1
        while A[right] == A[right - 1] and right >= i:
            right -= 1
        # print(left, right)
        A[right], A[left] = A[left], A[right]
        return A
