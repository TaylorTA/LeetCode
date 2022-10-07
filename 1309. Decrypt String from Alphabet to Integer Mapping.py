class Solution:
    def freqAlphabets(self, s: str) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        dic = {}
        i = 1
        for l in letters:
            dic[i] = l
            i += 1
        
        stack = list(s)
        
        op = ""
                
        while stack:
            c = stack.pop()
            
            if c == '#': 
                n = stack.pop() + stack.pop()
                op += dic[int(n[::-1])]
            else:
                op += dic[int(c)]
                
        return op[::-1]
