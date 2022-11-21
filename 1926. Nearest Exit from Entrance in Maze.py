class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        cx = entrance[0]
        cy = entrance[1]
        maze[cx][cy] = '+'
        q = collections.deque()
        q.append([cx, cy, 0])

        while q:
            cx, cy, d = q.popleft()
            #print(cx,cy)
            if 0 <= cx-1 < m and maze[cx-1][cy] == '.':
                if cx-1 ==0 or cy == 0 or cy == n-1:
                    return d+1
                else:
                    maze[cx-1][cy] = '+'
                    q.append([cx-1, cy, d+1])
            
            if cx+1 < m and maze[cx+1][cy] == '.':
                if cx+1 == m-1 or cy ==0 or cy == n-1:
                    return d+1
                else:
                    maze[cx+1][cy] = '+'
                    q.append([cx+1, cy, d+1])
            
            if 0 <= cy-1 and maze[cx][cy-1] == '.':
                if cy-1 == 0 or cx == 0 or cx == m-1:
                    return d+1
                else:
                    maze[cx][cy-1] = '+'
                    q.append([cx, cy-1, d+1])
            
            if cy+1 < n and maze[cx][cy+1] == '.':
                if cy+1 == n-1 or cx == 0 or cx == m-1:
                    return d+1
                else:
                    maze[cx][cy+1] = '+'
                    q.append([cx, cy+1, d+1])
            
        return -1
