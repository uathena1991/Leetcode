class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        lidx, ridx = 0, len(height) - 1
        max_left, max_right = 0, 0 # assume you add boarder height of 0 on two sides
        while lidx < ridx:
            max_left = max(max_left, height[lidx])
            max_right = max(max_right, height[ridx])
            if max_left < max_right:
                res += max_left - height[lidx]
                lidx += 1
            else:
                res += max_right - height[ridx]
                ridx -= 1

        return res

