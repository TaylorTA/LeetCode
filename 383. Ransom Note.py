class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)

        for c in r:
            if c not in m or m[c]<r[c]:
                return False
        
        return True
