class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        d = 0
        for i in range(len(strs[0])):
            l = [s[i] for s in strs]
            if  not all(l[i] <= l[i+1] for i in range(len(l) - 1)):
                d += 1
        return d
