class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        cs = 0
        m = nums[0]
        for i in range(n):
            cs += nums[i]
            m = max(m, cs)
            cs = max(0, cs)
        
        rm = [0]*n
        rm[-1] = nums[-1]
        rs = nums[n-1]
        for i in range(n-2, -1, -1):
            rs += nums[i]
            rm[i] = max(rm[i+1],rs)
        
        cm = -math.inf
        ls = 0
        for i in range(n):
            ls += nums[i]
            if i < n-1:
                cm = max(cm, ls+rm[i+1])

        return max(m, cm)
