class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        
        force = [0] * n
        
        f = 0
        for i in range(n):
            if dominoes[i] == 'R':
                f = n
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] += f
        
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'R':
                f = 0
            elif dominoes[i] == 'L':
                f = n
            else:
                f = max(f-1, 0)
            force[i] -= f
        
        op = ""
        for f in force:
            if f > 0:
                op += "R"
            elif f< 0:
                op += "L"
            else:
                op += "."
                
        return op
