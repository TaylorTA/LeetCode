class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 3:
            return len(s)
        
        window = {}
        left = 0
        window[s[0]] = 0
        window[s[1]] = 1
        maxLength = 2
        currLength = 2
        
        for i in range(2,len(s)):
            window[s[i]] = i
            
            if len(window) == 3:
                popItem = min(window, key=window.get)
                popIndex = window[popItem]
                window.pop(popItem)
                left = popIndex + 1
                
            maxLength = max(maxLength, i-left+1)
        
        return maxLength
