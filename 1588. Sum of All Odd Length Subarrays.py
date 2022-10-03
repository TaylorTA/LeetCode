class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        
        for i, n in enumerate(arr):
            s += ((i+1) * (len(arr)-i) + 1)//2 * n
        
        return s
