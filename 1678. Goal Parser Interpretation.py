class Solution:
    def interpret(self, command: str) -> str:
        op = ""
        
        for i,c in enumerate(command):
            if c == "G":
                op += "G"
            elif c == "(":
                if command[i+1] == "a":
                    op += "al"
                else:
                    op += "o"
        
        return op
