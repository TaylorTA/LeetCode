class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        ls = 0
        rs = sum(nums)
        m = math.inf
        mi = 0

        for i, n in enumerate(nums):
            ls += n
            rs -= n
            #print(ls, rs, i, n)
            if len(nums) - i - 1 == 0:
                c = ls//(i+1)
            else:
                c = abs(ls//(i+1) - rs//(len(nums) - i - 1))
            #print(c)
            if c < m:
                m = c
                mi = i
        
        return mi
