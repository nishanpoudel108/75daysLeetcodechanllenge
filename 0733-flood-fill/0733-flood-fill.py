class Solution(object):
    def floodFill(self, image, sr, sc, color):
        rows = len(image)
        cols = len(image[0])

        original = image[sr][sc]

        # If the color is already same, no need to process
        if original == color:
            return image

        def dfs(r, c):
            # Check boundaries
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Process only cells with original color
            if image[r][c] != original:
                return

            # Change color
            image[r][c] = color

            # Visit 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image