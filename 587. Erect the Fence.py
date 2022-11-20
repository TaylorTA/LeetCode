import numpy as np
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) == 1:
            return trees
            
        stack = []
        trees.sort(key = lambda x: [x[0], x[1]])
        top = trees.pop(0)

        def slope(p):
            if p[0] == top[0]:
                if p[1] > top[1]:
                    return 1E9
                else:
                    return -1E9
            else:
                return (p[1]-top[1])/(p[0]-top[0])
            
        trees.sort(key = lambda x: [slope(x), abs(x[0] - top[0]) + abs(x[1] - top[1])])

        index = len(trees) - 2
        while index >= 0 and slope(trees[index]) == slope(trees[-1]):
            index -= 1
        
        index += 1
        trees = trees[:index] + trees[index:][::-1]
        def getcross(p1, p2, p3):
            a = [(p2[0]-p1[0]), (p2[1]-p1[1])]
            b = [(p3[0]-p2[0]), (p3[1]-p2[1])]
            return np.cross(a,b)

        stack.append(top)
        for t in trees:
            stack.append(t)
            while len(stack) > 2 and getcross(stack[-3],stack[-2],stack[-1]) < 0:
                stack.pop(-2)
            
        return stack
