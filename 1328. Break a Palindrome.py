class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        op = ""
        if len(palindrome) <= 1:
            return op
        
        for i in range(len(palindrome)//2):
            if palindrome[i] > 'a':
                op = palindrome[:i] + 'a' + palindrome[i+1:]
                break
        
        if op == "":
            op = palindrome[:-1] + "b"
        
        return op
