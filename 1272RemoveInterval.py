class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        output = []
        
        for x,y in intervals:
            if x > toBeRemoved[1] or y < toBeRemoved[0]:
                output.append([x,y])
            else:
                if x < toBeRemoved[0]:
                    output.append([x, toBeRemoved[0]])
                if y > toBeRemoved[1]:
                    output.append([toBeRemoved[1], y])
                    
        return output
