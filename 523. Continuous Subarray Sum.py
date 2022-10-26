class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = defaultdict(int)
        d[0] = 0
        s = 0
        
        for i, n in enumerate(nums):
            s += n
            if s % k not in d:
                d[s%k] = i+1
            elif d[s%k] <= i-1:
                return True
        return False
        
