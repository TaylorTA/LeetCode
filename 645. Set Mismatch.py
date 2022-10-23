class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = [False] * (len(nums)+1)
        op = [0, 0]
        for n in nums:
            if seen[n]:
                op[0] = n
            seen[n] = True
        
        for i, n in enumerate(seen, start = 1):
            if not n:
                op[1] = i - 1
        
        return op
