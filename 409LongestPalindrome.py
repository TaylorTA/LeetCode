class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        numOdd = 0   
        length = 0
        freq = {}
        
        for c in s:
            if c in freq:
                freq[c] = freq[c] + 1
                if freq[c]%2 == 0:
                    length += 2
                    numOdd -=1
                else:
                    numOdd +=1
            else:
                freq[c] = 1
                numOdd +=1
        
        if numOdd > 0:
            length += 1
        
        return length
