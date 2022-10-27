class Solution:
    def floodFill(self, image, sr, sc, color):
        if image[sr][sc] == color:
            return image
        stack, currentcolor = [(sr,sc)], image[sr][sc]
        while stack:
            point = stack.pop()  # pop the point
            image[point[0]][point[1]] = color  # fill color
            for x, y in zip((point[0],point[0],point[0]+1,point[0]-1),
                            (point[1]+1,point[1]-1,point[1],point[1])):
                if 0<=x<len(image) and 0<=y<len(image[0]) and image[x][y] == currentcolor:
                    stack.append((x,y))
        return image


# test
input_image = [[1,1,1],[1,1,0],[1,0,1]]
expected_output = [[2,2,2],[2,2,0],[2,0,1]]
s = Solution()
if s.floodFill(input_image,1,1,2) == expected_output:
    print("test passed")