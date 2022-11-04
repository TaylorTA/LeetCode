class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        v = []
        cur = len(s) - 1

        for i, c in enumerate(s):
            if cur <= i:
                break
            if c in vowels:
                while s[cur] not in vowels and cur > i:
                    cur -= 1
                
                #print(cur)
                s = s[0:i] + s[cur] + s[i+1:]
                s = s[0:cur] + c + s[cur+1:]
                cur -= 1
        
        return s
