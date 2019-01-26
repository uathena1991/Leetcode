class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image or not image[0]:
            return image

        queue = [(sr, sc)]
        old_color = image[sr][sc]
        if old_color == newColor:
            return image

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while queue:
            cr,cc = queue.pop(0)
            image[cr][cc] = newColor
            for dx, dy in dirs:
                nx, ny = cr + dx , cc + dy
                if (0 <= nx < len(image)) and (0 <= ny < len(image[0])) and image[nx][ny] == old_color:
                    queue.append((nx,ny))

        return image

