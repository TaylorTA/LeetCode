class Solution:
    def futherFill(self, image, sr, sc, color, icolor):
        if image[sr][sc] == icolor:
            image[sr][sc] = color
            
            if sr-1 >= 0:
                self.futherFill(image, sr-1, sc, color, icolor)
            if sr+1 < len(image):
                self.futherFill(image, sr+1, sc, color, icolor)
            if sc-1 >= 0:
                self.futherFill(image, sr, sc-1, color, icolor)
            if sc+1 < len(image[0]):
                self.futherFill(image, sr, sc+1, color, icolor)
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image
        self.futherFill(image, sr, sc, color, image[sr][sc])
        return image
        
