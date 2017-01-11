class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_l = 0
        max_r = 0
        l_idx = 0
        r_idx = len(height)-1
        max_area = min(height[l_idx],height[r_idx])*(r_idx-l_idx)
        while l_idx < r_idx:
            if height[l_idx] < height[r_idx]:
                l_idx += 1
            else:
                r_idx -= 1
            tmp = min(height[l_idx],height[r_idx])*(r_idx-l_idx)
            if tmp > max_area:
                max_area = tmp
                max_l = l_idx
                max_r = r_idx
        return max_area

            