class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        op = ""
        for word in words:
            op += word[::-1] + " "
        
        return op[:-1]
