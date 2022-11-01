class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        result = [-1] * len(grid[0])
        
        for j in range(len(grid[0])):
            #print(j)
            curc = j
            for i in range(len(grid)):
                if grid[i][curc] == 1:
                    if curc < len(grid[0])-1 and grid[i][curc+1] == 1:
                        curc += 1
                    else:
                        result[j] = -1
                        break
                else:
                    if curc != 0 and grid[i][curc-1] == -1:
                        curc -= 1
                    else:
                        result[j] = -1
                        break
                #print(curc)
                result[j] = curc
            #print()
        
        return result
