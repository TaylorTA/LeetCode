class Solution:
    def dps(self, graph, marks, node, mark):
        if marks[node] == -1:
            marks[node] = mark
            for n in graph[node]:
                self.dps(graph, marks, n, mark)
    
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = [[] for _ in range(26)]
        
        for e in equations:
            if e[1] == '=':
                x = ord(e[0]) - ord('a')
                y = ord(e[3]) - ord('a')
                graph[x].append(y)
                graph[y].append(x)
        
        marks = [-1] * 26
        
        mark = 0
        for node in range(len(graph)):
            self.dps(graph, marks, node, mark)
            mark += 1
        
        # print(marks)
        
        for e in equations:
            if e[1] == '!':
                x = ord(e[0]) - ord('a')
                y = ord(e[3]) - ord('a')
                if marks[x] == marks[y]:
                    return False
        
        return True
