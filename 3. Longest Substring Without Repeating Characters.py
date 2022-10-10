class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashmap = defaultdict(int)
        curr = 0
        left = 0
        
        for c in s:
            if c not in hashmap:
                hashmap[c] += 1
                curr += 1
            else:
                l = max(l, curr)
                while s[left] != c:
                    hashmap.pop(s[left])
                    left += 1
                    curr -= 1
                # print(hashmap)
                left += 1
        
        return max(l,curr)
