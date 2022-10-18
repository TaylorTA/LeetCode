class Solution:
    def countAndSay(self, n: int) -> str:
        op = "1"
        
        for _ in range(n-1):
            cur = ""
            i = 0
            j = 0
            while i < len(op):
                while j < len(op) and op[i] == op[j]:
                    j += 1
                cur += str(j-i) + op[i]
                i = j
            op = cur
        
        return op
